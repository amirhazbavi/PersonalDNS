from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List

from app.core.db import get_db
from app.core.security import hash_password, verify_password, create_access_token, generate_verification_token
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.user import UserRegister, UserLogin, UserOut, TokenResponse
from app.services.auth_service import AuthService
from app.services.audit_service import audit_log
from app.core.cache import CacheService

router = APIRouter(prefix="/api/auth", tags=["auth"])
auth_service = AuthService()

@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserRegister, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if email exists
    existing_user = db.query(User).filter(User.email == payload.email.lower()).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create user
    user = User(
        email=payload.email.lower(),
        password_hash=hash_password(payload.password),
        full_name=payload.full_name,
        is_active=True,
        is_verified=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    # Generate token
    token = create_access_token(str(user.id))
    
    # Audit log
    audit_log(db, user.id, "user_register", {"email": user.email})
    
    # Send verification email in background
    background_tasks.add_task(auth_service.send_verification_email, user.email, user.id)
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": 3600
    }

@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    """Login user"""
    user = db.query(User).filter(User.email == payload.email.lower()).first()
    
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    if not user.is_active or user.is_deleted:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive or deleted"
        )
    
    if user.two_fa_enabled:
        # Return a temporary token for 2FA verification
        temp_token = create_access_token(str(user.id), expires_delta=None)
        return {
            "access_token": temp_token,
            "token_type": "bearer_2fa",
            "expires_in": 300
        }
    
    # Generate token
    token = create_access_token(str(user.id))
    
    # Update last login
    user.last_login = datetime.utcnow()
    db.commit()
    
    # Audit log
    audit_log(db, user.id, "user_login", {"email": user.email})
    
    # Clear cache
    CacheService.delete(f"user:{user.id}")
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": 3600
    }

@router.get("/me", response_model=UserOut)
def get_profile(current_user: User = Depends(get_current_user)):
    """Get current user profile"""
    return current_user

@router.post("/logout")
def logout(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Logout user"""
    audit_log(db, current_user.id, "user_logout", {})
    CacheService.delete(f"user:{current_user.id}")
    return {"message": "Logged out successfully"}

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(current_user: User = Depends(get_current_user)):
    """Refresh access token"""
    token = create_access_token(str(current_user.id))
    return {
        "access_token": token,
        "token_type": "bearer",
        "expires_in": 3600
    }

@router.post("/change-password")
def change_password(
    old_password: str,
    new_password: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Change user password"""
    if not verify_password(old_password, current_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid current password"
        )
    
    current_user.password_hash = hash_password(new_password)
    db.commit()
    
    audit_log(db, current_user.id, "password_changed", {})
    CacheService.delete(f"user:{current_user.id}")
    
    return {"message": "Password changed successfully"}

@router.post("/request-password-reset")
def request_password_reset(
    email: str,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Request password reset"""
    user = db.query(User).filter(User.email == email.lower()).first()
    if user:
        reset_token = generate_verification_token()
        # Store reset token in cache (expires in 15 minutes)
        CacheService.set(f"password_reset:{user.id}", reset_token, ttl=900)
        background_tasks.add_task(auth_service.send_password_reset_email, user.email, reset_token)
    
    return {"message": "If email exists, password reset link has been sent"}

@router.post("/reset-password")
def reset_password(
    token: str,
    new_password: str,
    db: Session = Depends(get_db)
):
    """Reset password with token"""
    # Validate token format and find user
    # This is simplified - in production, validate token properly
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
