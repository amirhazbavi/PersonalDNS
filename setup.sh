#!/bin/bash
set -e

echo "🚀 PersonalDNS Setup"
echo "==================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Create .env files
echo "📝 Creating environment files..."

if [ ! -f "backend/.env" ]; then
    cp backend/.env.example backend/.env
    echo "✅ Created backend/.env"
else
    echo "⚠️  backend/.env already exists"
fi

if [ ! -f "frontend/.env" ]; then
    cp frontend/.env.example frontend/.env
    echo "✅ Created frontend/.env"
else
    echo "⚠️  frontend/.env already exists"
fi

echo ""
echo "🐳 Starting Docker containers..."
echo ""

# Start services
docker compose up -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

echo ""
echo "✅ PersonalDNS is starting!"
echo ""
echo "📋 Service URLs:"
echo "   Frontend:   http://localhost:80"
echo "   Backend:    http://localhost:8000"
echo "   API Docs:   http://localhost:8000/api/docs"
echo "   PowerDNS:   http://localhost:8081"
echo "   Prometheus: http://localhost:9090"
echo "   Grafana:    http://localhost:3001"
echo ""
echo "🔍 Check logs with:"
echo "   docker compose logs -f backend"
echo ""
echo "⏹️  Stop services with:"
echo "   docker compose down"
echo ""
