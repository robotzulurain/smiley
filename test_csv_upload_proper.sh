#!/bin/bash
echo "=== Testing CSV Upload Endpoint (Proper) ==="

BACKEND_URL="https://smiley-q2wz.onrender.com"

echo "1. Testing with proper headers..."
# Create a sample CSV
cat > proper_test.csv << 'SAMPLE'
organism,antibiotic,susceptibility,specimen_type,facility,test_date
E. coli,Amoxicillin,R,Urine,Central Hospital,2024-01-15
S. aureus,Ciprofloxacin,S,Blood,City Lab,2024-01-16
K. pneumoniae,Gentamicin,I,Sputum,Regional Center,2024-01-17
SAMPLE

echo -e "\n2. Uploading with proper multipart form data..."
curl -v -X POST "$BACKEND_URL/api/upload/csv" \
  -F "file=@proper_test.csv" \
  -H "Origin: https://amrfrontend.netlify.app" \
  -H "Accept: application/json" \
  -H "User-Agent: Mozilla/5.0"

echo -e "\n\n3. Testing with different approach..."
# Alternative: use --form instead of -F
curl -X POST "$BACKEND_URL/api/upload/csv" \
  --form "file=@proper_test.csv" \
  -H "Origin: https://amrfrontend.netlify.app"

echo -e "\n4. Test Complete!"
