#!/bin/bash
echo "=== Testing Frontend Connection ==="

FRONTEND_URL="https://amrfrontend.netlify.app"
BACKEND_URL="https://smiley-q2wz.onrender.com"

echo "1. Testing frontend accessibility..."
curl -s -I "$FRONTEND_URL" | head -1

echo -e "\n2. Testing backend connectivity from frontend perspective..."
# This simulates what the frontend would experience
curl -s -H "Origin: $FRONTEND_URL" -H "Access-Control-Request-Method: GET" -H "Access-Control-Request-Headers: X-Requested-With" -X OPTIONS "$BACKEND_URL/api/health/"

echo -e "\n3. Checking if frontend can reach backend..."
curl -s "$BACKEND_URL/api/health/" -H "Origin: $FRONTEND_URL"

echo -e "\n\n4. Frontend Test Complete!"
echo "Visit $FRONTEND_URL to check One Health components and filters manually."
