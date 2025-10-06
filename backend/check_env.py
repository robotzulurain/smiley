import os

print("=== Environment Variables ===")
for key, value in os.environ.items():
    if 'DATABASE' in key or 'SECRET' in key or 'DEBUG' in key:
        print(f"{key}: {value}")

print(f"\nDATABASE_URL exists: {'DATABASE_URL' in os.environ}")
if 'DATABASE_URL' in os.environ:
    db_url = os.environ['DATABASE_URL']
    # Mask password for security
    if '@' in db_url:
        parts = db_url.split('@')
        user_pass = parts[0]
        if ':' in user_pass:
            user, password = user_pass.split(':', 1)
            masked_url = f"{user}:****@{parts[1]}"
            print(f"DATABASE_URL: {masked_url}")
        else:
            print(f"DATABASE_URL: {db_url}")
    else:
        print(f"DATABASE_URL: {db_url}")
