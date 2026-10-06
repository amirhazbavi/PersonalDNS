#!/bin/bash

# PersonalDNS - Complete Installation and Startup Script

set -e

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║          🚀 PersonalDNS - Installation & Setup 🚀             ║"
echo "║                                                                ║"
echo "║     Production-ready multi-user DNS management platform       ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check system requirements
echo "${BLUE}📋 Checking system requirements...${NC}"
echo ""

if ! command -v docker &> /dev/null; then
    echo "${RED}❌ Docker is not installed${NC}"
    echo "   Please install Docker from https://www.docker.com/products/docker-desktop"
    exit 1
fi
echo "${GREEN}✅ Docker ${NC}($(docker --version | grep -oP 'Docker version \K[0-9]+\.[0-9]+'))"

if ! command -v docker-compose &> /dev/null; then
    echo "${RED}❌ Docker Compose is not installed${NC}"
    echo "   Please install Docker Compose"
    exit 1
fi
echo "${GREEN}✅ Docker Compose ${NC}($(docker-compose --version | grep -oP 'docker-compose version \K[0-9]+\.[0-9]+'))"

if ! command -v git &> /dev/null; then
    echo "${RED}❌ Git is not installed${NC}"
    echo "   Please install Git from https://git-scm.com/"
    exit 1
fi
echo "${GREEN}✅ Git ${NC}($(git --version | grep -oP 'git version \K[0-9]+\.[0-9]+'))"

echo ""
echo "${BLUE}📂 Checking directory structure...${NC}"
echo ""

if [ ! -d "backend" ]; then
    echo "${RED}❌ backend/ directory not found${NC}"
    exit 1
fi
echo "${GREEN}✅ backend/ ${NC}"

if [ ! -d "frontend" ]; then
    echo "${RED}❌ frontend/ directory not found${NC}"
    exit 1
fi
echo "${GREEN}✅ frontend/ ${NC}"

if [ ! -d "powerdns" ]; then
    echo "${RED}❌ powerdns/ directory not found${NC}"
    exit 1
fi
echo "${GREEN}✅ powerdns/ ${NC}"

if [ ! -f "docker-compose.yml" ]; then
    echo "${RED}❌ docker-compose.yml not found${NC}"
    exit 1
fi
echo "${GREEN}✅ docker-compose.yml ${NC}"

echo ""
echo "${BLUE}⚙️  Setting up environment files...${NC}"
echo ""

# Backend .env
if [ ! -f "backend/.env" ]; then
    if [ -f "backend/.env.example" ]; then
        cp backend/.env.example backend/.env
        echo "${GREEN}✅ Created backend/.env ${NC}(from example)"
    else
        echo "${RED}❌ backend/.env.example not found${NC}"
        exit 1
    fi
else
    echo "${YELLOW}⚠️  backend/.env already exists ${NC}(skipping)"
fi

# Frontend .env
if [ ! -f "frontend/.env" ]; then
    if [ -f "frontend/.env.example" ]; then
        cp frontend/.env.example frontend/.env
        echo "${GREEN}✅ Created frontend/.env ${NC}(from example)"
    fi
else
    echo "${YELLOW}⚠️  frontend/.env already exists ${NC}(skipping)"
fi

echo ""
echo "${BLUE}🔒 Generating secure keys...${NC}"
echo ""

SECRET_KEY=$(openssl rand -hex 32)
sed -i.bak "s/SECRET_KEY=.*/SECRET_KEY=${SECRET_KEY}/" backend/.env
echo "${GREEN}✅ Generated SECRET_KEY ${NC}"

echo ""
echo "${BLUE}🐳 Pulling Docker images...${NC}"
echo ""

docker compose pull --quiet
echo "${GREEN}✅ Docker images pulled ${NC}"

echo ""
echo "${BLUE}🚀 Starting services...${NC}"
echo ""

docker compose up -d

echo ""
echo "${BLUE}⏳ Waiting for services to be ready...${NC}"
echo ""

# Wait for backend
echo "   Waiting for Backend..."
for i in {1..30}; do
    if curl -s http://localhost:8000/api/health > /dev/null; then
        echo "${GREEN}✅ Backend is ready${NC}"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "${RED}❌ Backend failed to start${NC}"
        docker compose logs backend
        exit 1
    fi
    sleep 1
done

# Wait for Frontend
echo "   Waiting for Frontend..."
for i in {1..30}; do
    if curl -s http://localhost/ > /dev/null; then
        echo "${GREEN}✅ Frontend is ready${NC}"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "${RED}❌ Frontend failed to start${NC}"
        docker compose logs nginx
        exit 1
    fi
    sleep 1
done

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   ✅ Setup Complete! ✅                        ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "${GREEN}🌐 Access PersonalDNS:${NC}"
echo ""
echo "   ${BLUE}Frontend:${NC}        http://localhost"
echo "   ${BLUE}Backend API:${NC}     http://localhost:8000"
echo "   ${BLUE}API Docs:${NC}       http://localhost:8000/api/docs"
echo "   ${BLUE}PowerDNS Admin:${NC}  http://localhost:8081"
echo "   ${BLUE}Prometheus:${NC}      http://localhost:9090"
echo "   ${BLUE}Grafana:${NC}         http://localhost:3001 (admin/admin)"
echo ""
echo "${GREEN}📝 First Steps:${NC}"
echo ""
echo "   1. Open http://localhost in your browser"
echo "   2. Click 'ثبت‌نام' (Register) to create account"
echo "   3. Login with your email"
echo "   4. Add your first domain"
echo ""
echo "${GREEN}📊 Monitor Services:${NC}"
echo ""
echo "   View logs:        ${BLUE}docker compose logs -f backend${NC}"
echo "   Check status:     ${BLUE}docker compose ps${NC}"
echo "   Stop services:    ${BLUE}docker compose down${NC}"
echo ""
echo "${GREEN}💡 Need Help?${NC}"
echo ""
echo "   View all commands:        ${BLUE}cat QUICKSTART.md${NC}"
echo "   Check backend logs:       ${BLUE}docker compose logs -f backend${NC}"
echo "   Connect to database:      ${BLUE}docker compose exec postgres psql -U pdnsuser -d personaldns${NC}"
echo ""
echo "${BLUE}Made with ❤️ for Iran - سازنده شده برای ایران${NC}"
echo ""
