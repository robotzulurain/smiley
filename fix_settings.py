# Read current settings
with open('amr_project/settings.py', 'r') as f:
    content = f.read()

# Remove any existing Render database config at the bottom
import re
content = re.sub(r'# Render PostgreSQL database configuration.*?ssl_require=True.*?\n.*?\}', '', content, flags=re.DOTALL)

# Add imports at the top after the initial comments
lines = content.split('\n')
new_lines = []
import_added = False

for line in lines:
    if not import_added and ('from pathlib import Path' in line or 'BASE_DIR' in line):
        new_lines.append('import os')
        new_lines.append('import dj_database_url')
        new_lines.append('')
        import_added = True
    new_lines.append(line)

content = '\n'.join(new_lines)

# Replace DATABASES section
old_db = '''DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}'''

new_db = '''DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Render PostgreSQL configuration
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True
        )
    }'''

content = content.replace(old_db, new_db)

# Write fixed content
with open('amr_project/settings.py', 'w') as f:
    f.write(content)

print("✅ Settings fixed successfully!")
