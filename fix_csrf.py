import re

# Read the current views.py
with open('backend/amr_api/views.py', 'r') as f:
    content = f.read()

# Add the import at the top if not present
if 'from django.views.decorators.csrf import csrf_exempt' not in content:
    content = content.replace(
        'from django.http import JsonResponse',
        'from django.http import JsonResponse\nfrom django.views.decorators.csrf import csrf_exempt'
    )

# Add the decorator to upload_csv function
content = re.sub(
    r'def upload_csv\(request\):',
    '@csrf_exempt\ndef upload_csv(request):',
    content
)

# Write back the fixed content
with open('backend/amr_api/views.py', 'w') as f:
    f.write(content)

print("✅ CSRF exemption added to upload_csv view")
