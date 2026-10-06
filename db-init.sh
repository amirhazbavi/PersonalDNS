#!/bin/bash

echo "📊 PersonalDNS Database Setup"
echo "============================="
echo ""

# Wait for PostgreSQL
echo "⏳ Waiting for PostgreSQL..."
sleep 5

# Run migrations (if using Alembic)
echo "🔄 Running database migrations..."
docker compose exec backend alembic upgrade head

echo ""
echo "✅ Database setup completed"
