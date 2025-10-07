import re

# Read the current production settings
with open('backend/amr_project/settings_production.py', 'r') as f:
    content = f.read()

# Add CSRF_TRUSTED_ORIGINS if not present
if 'CSRF_TRUSTED_ORIGINS' not in content:
    # Find a good place to insert it - after ALLOWED_HOSTS
    content = content.replace(
        "ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.onrender.com,localhost,127.0.0.1').split(',')",
        "ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '.onrender.com,localhost,127.0.0.1').split(',')\n\n# CSRF settings\nCSRF_TRUSTED_ORIGINS = [\n    'https://amrfrontend.netlify.app',\n    'https://smiley-q2wz.onrender.com',\n]"
    )

# Also ensure CORS is properly configured for CSRF
if "CORS_ALLOW_ALL_ORIGINS = True" not in content:
    # Add it after CORS_ALLOWED_ORIGINS
    content = content.replace(
        "CORS_ALLOWED_ORIGINS = [",
        "CORS_ALLOW_ALL_ORIGINS = True  # For development, you can restrict this in production\nCORS_ALLOWED_ORIGINS = ["
    )

# Write the fixed content back
with open('backend/amr_project/settings_production.py', 'w') as f:
    f.write(content)

print("✅ CSRF middleware settings updated")
