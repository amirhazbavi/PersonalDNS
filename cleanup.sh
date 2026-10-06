#!/bin/bash

echo "🗑️  Stopping PersonalDNS..."
docker compose down

echo "✅ All services stopped"
echo ""
echo "To remove volumes and data, run:"
echo "  docker compose down -v"
