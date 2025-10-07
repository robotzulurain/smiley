#!/bin/bash
echo "=== Testing CSV Upload Endpoint (Final) ==="

BACKEND_URL="https://smiley-q2wz.onrender.com"

# Test if the endpoint exists
echo "1. Testing CSV upload endpoint availability..."
curl -s -X OPTIONS "$BACKEND_URL/api/upload/csv" \
  -H "Origin: https://amrfrontend.netlify.app"

echo -e "\n2. Testing with a sample CSV file..."
# Create a sample CSV for testing
cat > sample_test.csv << 'SAMPLE'
organism,antibiotic,susceptibility,specimen_type,facility,test_date
E. coli,Amoxicillin,R,Urine,Central Hospital,2024-01-15
S. aureus,Ciprofloxacin,S,Blood,City Lab,2024-01-16
K. pneumoniae,Gentamicin,I,Sputum,Regional Center,2024-01-17
SAMPLE

echo -e "\n3. Uploading sample CSV (with CSRF exemption)..."
curl -s -X POST "$BACKEND_URL/api/upload/csv" \
  -F "file=@sample_test.csv" \
  -H "Origin: https://amrfrontend.netlify.app" \
  -H "X-CSRFToken: exempt" \
  -H "Content-Type: multipart/form-data"

echo -e "\n4. Final Health Check..."
curl -s "$BACKEND_URL/api/health/"

echo -e "\n5. Test Complete!"
