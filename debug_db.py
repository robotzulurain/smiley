import os
print("DATABASE_URL environment variable:", os.environ.get('DATABASE_URL', 'Not set'))
print("All environment variables:")
for key, value in os.environ.items():
    if 'DATABASE' in key or 'DB' in key or 'URL' in key:
        print(f"{key}: {value}")
