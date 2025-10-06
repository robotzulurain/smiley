#!/bin/bash
echo "=== Testing CSV Upload Endpoint ==="

BACKEND_URL="https://smiley-q2wz.onrender.com"

# Test if the endpoint exists
echo "1. Testing CSV upload endpoint availability..."
curl -s -X OPTIONS "$BACKEND_URL/api/upload/csv" -H "Origin: https://amrfrontend.netlify.app"

echo -e "\n2. Testing with a sample CSV file..."
# Create a sample CSV for testing
cat > sample_test.csv << 'SAMPLE'
organism,antibiotic,susceptibility,specimen_type,facility,test_date
E. coli,Amoxicillin,R,Urine,Central Hospital,2024-01-15
S. aureus,Ciprofloxacin,S,Blood,City Lab,2024-01-16
K. pneumoniae,Gentamicin,I,Sputum,Regional Center,2024-01-17
SAMPLE

# Test the upload (this will likely fail without proper auth, but tests the endpoint)
curl -s -X POST "$BACKEND_URL/api/upload/csv" \
  -F "file=@sample_test.csv" \
  -H "Origin: https://amrfrontend.netlify.app"

echo -e "\n3. CSV Upload Test Complete!"
