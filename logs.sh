#!/bin/bash

echo "📊 Showing PersonalDNS Container Logs"
echo "====================================="
echo ""

case "$1" in
    backend)
        docker compose logs -f backend
        ;;
    postgres)
        docker compose logs -f postgres
        ;;
    redis)
        docker compose logs -f redis
        ;;
    powerdns)
        docker compose logs -f powerdns
        ;;
    nginx)
        docker compose logs -f nginx
        ;;
    all)
        docker compose logs -f
        ;;
    *)
        echo "Available services:"
        echo "  ./logs.sh backend"
        echo "  ./logs.sh postgres"
        echo "  ./logs.sh redis"
        echo "  ./logs.sh powerdns"
        echo "  ./logs.sh nginx"
        echo "  ./logs.sh all"
        ;;
esac
