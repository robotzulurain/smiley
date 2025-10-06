#!/bin/bash
echo "Testing AMR Backend API..."

BASE_URL="https://smiley-q2wz.onrender.com"

echo "1. Testing health endpoint:"
curl -s "$BASE_URL/api/health/" | python3 -m json.tool

echo -e "\n2. Testing options endpoint:"
curl -s "$BASE_URL/api/options/" | python3 -m json.tool

echo -e "\n3. Testing root endpoint:"
curl -s "$BASE_URL/"

echo -e "\nAPI Test Complete!"
