import requests

url = "https://smiley-q2wz.onrender.com/api/upload/csv"

# Test 1: Simple POST without file
print("Test 1: POST without file")
response = requests.post(url)
print(f"Status: {response.status_code}")
print(f"Response: {response.text[:200]}")

# Test 2: POST with file
print("\nTest 2: POST with file")
files = {'file': ('test.csv', 'organism,antibiotic,susceptibility\nE. coli,Amoxicillin,R', 'text/csv')}
response = requests.post(url, files=files)
print(f"Status: {response.status_code}")
print(f"Response: {response.text[:500]}")
