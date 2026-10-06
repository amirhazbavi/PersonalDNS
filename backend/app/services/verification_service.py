from app.core.security import generate_verification_token

def verification_txt_value(token: str) -> str:
    """Generate TXT record value for domain verification"""
    return f"personaldns-verification={token}"

def generate_verification_token() -> str:
    """Generate a new verification token"""
    return generate_verification_token()
