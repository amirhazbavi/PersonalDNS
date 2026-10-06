# PersonalDNS - Setup Instructions

## 📋 Prerequisites

You need to have installed:
- Docker Desktop (includes Docker and Docker Compose)
- Git
- 2GB RAM minimum (4GB recommended)
- Available ports: 80, 443, 53, 8000, 3000

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/amirhazbavi/PersonalDNS.git
cd PersonalDNS
```

### 2. Setup and Run

#### Option A: Automatic Setup (Recommended)

```bash
# Make scripts executable
chmod +x setup.sh logs.sh status.sh cleanup.sh test-api.sh

# Run setup script
./setup.sh
```

#### Option B: Manual Setup

```bash
# Copy configuration files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit configuration if needed
nano backend/.env

# Start all services
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f backend
```

## 🔍 Access Services

After startup (wait 30-60 seconds for all services to be ready):

| Service | URL | Credentials |
|---------|-----|-------------|
| **Frontend** | http://localhost | - |
| **Backend API** | http://localhost:8000 | - |
| **API Documentation** | http://localhost:8000/api/docs | - |
| **PowerDNS Admin** | http://localhost:8081 | API Key in .env |
| **Prometheus** | http://localhost:9090 | - |
| **Grafana** | http://localhost:3001 | admin / admin |
| **PostgreSQL** | localhost:5432 | pdnsuser / pdns_secure_password_123 |
| **Redis** | localhost:6379 | password: redis_secure_password_123 |

## 📝 First Steps

### 1. Test the Backend

```bash
# Make test script executable
chmod +x test-api.sh

# Run API tests
./test-api.sh
```

### 2. Create Your First Domain

```bash
# Register a user
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "you@example.com",
    "password": "SecurePass123",
    "full_name": "Your Name"
  }'

# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "you@example.com",
    "password": "SecurePass123"
  }'

# Add a domain (use TOKEN from login response)
curl -X POST http://localhost:8000/api/domains \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "example.com"}'
```

## 🛠️ Common Commands

### View Logs

```bash
# Backend logs
docker compose logs -f backend

# PowerDNS logs
docker compose logs -f powerdns

# PostgreSQL logs
docker compose logs -f postgres

# All logs
docker compose logs -f
```

### Check Status

```bash
# Container status
docker compose ps

# Full status
./status.sh
```

### Database Access

```bash
# Connect to PostgreSQL
docker compose exec postgres psql -U pdnsuser -d personaldns

# Common queries:
# \dt              - List tables
# SELECT * FROM users;        - List users
# SELECT * FROM domains;      - List domains
# \q               - Exit
```

### Redis Access

```bash
# Connect to Redis
docker compose exec redis redis-cli -a redis_secure_password_123

# Common commands:
# PING            - Test connection
# KEYS *          - List all keys
# GET key_name    - Get value
# DEL key_name    - Delete key
```

## 🧹 Stopping Services

```bash
# Stop all services (keeps data)
docker compose down

# Stop and remove all data
docker compose down -v

# Or use cleanup script
./cleanup.sh
```

## 🔧 Configuration

### Edit Backend Settings

```bash
nano backend/.env
```

Key settings:
- `DATABASE_URL` - PostgreSQL connection
- `REDIS_URL` - Redis connection
- `POWERDNS_API_KEY` - PowerDNS API key
- `SECRET_KEY` - JWT secret (change in production!)
- `FRONTEND_URL` - Frontend URL

### Edit Frontend Settings

```bash
nano frontend/.env
```

## 🚀 Production Deployment

For production on a VPS, see [DEPLOYMENT.md](DEPLOYMENT.md)

## 📊 Monitoring

### Prometheus Metrics

```bash
# Access Prometheus
open http://localhost:9090

# Example queries:
# - up{job="backend"}
# - rate(http_requests_total[5m])
```

### Grafana Dashboards

```bash
# Access Grafana
open http://localhost:3001

# Login: admin / admin
# Configure data source: Prometheus at http://prometheus:9090
```

## 🆘 Troubleshooting

### Services won't start

```bash
# Check Docker daemon
docker ps

# Increase Docker memory limit if needed
# On Mac/Windows: Docker Desktop > Preferences > Resources

# Rebuild containers
docker compose down
docker system prune -a
docker compose up -d
```

### Port already in use

```bash
# Check which process uses port
lsof -i :8000
lsof -i :80
lsof -i :53

# Kill process
kill -9 PID
```

### Database connection error

```bash
# Wait longer for PostgreSQL to start
sleep 30
docker compose logs postgres

# Reset database
docker compose down -v
docker compose up -d
```

### Backend crashes immediately

```bash
# Check backend logs
docker compose logs backend

# Check if .env file is correct
cat backend/.env

# Verify database is running
docker compose ps postgres
```

## 📚 Documentation

- [API Documentation](docs/API.md)
- [Database Schema](docs/DATABASE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Iran Registrar Integration](docs/IRAN_REGISTRAR.md)

## 🤝 Support

- GitHub Issues: https://github.com/amirhazbavi/PersonalDNS/issues
- Email: support@personaldns.ir
- Telegram: @personaldns_support

## 📄 License

MIT License - See LICENSE file
