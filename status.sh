#!/bin/bash

echo "🔍 PersonalDNS System Status"
echo "============================"
echo ""

echo "📦 Docker Containers:"
docker compose ps

echo ""
echo "💾 Docker Volumes:"
docker volume ls | grep personaldns

echo ""
echo "🌐 Network:"
docker network ls | grep personaldns

echo ""
echo "📈 Resource Usage:"
docker stats --no-stream
