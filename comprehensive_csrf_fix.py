import re

# Read the current views.py
with open('backend/amr_api/views.py', 'r') as f:
    content = f.read()

# Ensure we have the csrf_exempt import
if 'from django.views.decorators.csrf import csrf_exempt' not in content:
    # Add it after the JsonResponse import
    content = content.replace(
        'from django.http import JsonResponse',
        'from django.http import JsonResponse\nfrom django.views.decorators.csrf import csrf_exempt'
    )

# Ensure the decorator is properly applied to upload_csv
if '@csrf_exempt' not in content or 'def upload_csv' not in content:
    # If the decorator is missing, add it
    content = re.sub(
        r'(def upload_csv\(request\):)',
        r'@csrf_exempt\n\\1',
        content
    )

# Write the fixed content back
with open('backend/amr_api/views.py', 'w') as f:
    f.write(content)

print("✅ Comprehensive CSRF fix applied")
