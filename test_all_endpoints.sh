#!/bin/bash
echo "=== Testing All AMR API Endpoints ==="

BASE_URL="https://smiley-q2wz.onrender.com"

endpoints=(
    "/api/health/"
    "/api/options/"
    "/api/summary/counts-summary"
    "/api/summary/time-trends" 
    "/api/summary/antibiogram"
    "/api/summary/sex-age"
    "/api/geo/facilities"
)

for endpoint in "${endpoints[@]}"; do
    echo "Testing: $endpoint"
    response=$(curl -s -w "HTTP_STATUS:%{http_code}" "${BASE_URL}${endpoint}")
    
    # Extract the body and status code
    body=$(echo "$response" | sed -e 's/HTTP_STATUS\:.*//g')
    status=$(echo "$response" | tr -d '\n' | sed -e 's/.*HTTP_STATUS://')
    
    if [ "$status" = "200" ]; then
        echo "✅ Status: $status"
        echo "$body" | python3 -m json.tool 2>/dev/null || echo "$body"
    else
        echo "❌ Status: $status"
        echo "$body"
    fi
    echo "---"
done
