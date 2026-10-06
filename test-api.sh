#!/bin/bash
set -e

echo "🧪 Testing PersonalDNS API"
echo "=========================="
echo ""

API_URL="http://localhost:8000/api"

# Health check
echo "1️⃣  Health Check:"
curl -s $API_URL/health | jq . || echo "Backend not ready"
echo ""

# Register user
echo "2️⃣  Register User:"
RESP=$(curl -s -X POST $API_URL/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email":"test@example.com",
    "password":"TestPass123",
    "full_name":"Test User"
  }')
echo $RESP | jq .
TOKEN=$(echo $RESP | jq -r '.access_token')
echo ""

# Get profile
echo "3️⃣  Get Profile:"
curl -s -H "Authorization: Bearer $TOKEN" $API_URL/auth/me | jq .
echo ""

# List domains
echo "4️⃣  List Domains:"
curl -s -H "Authorization: Bearer $TOKEN" $API_URL/domains | jq .
echo ""

echo "✅ API tests completed"
