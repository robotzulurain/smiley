# Read current urls.py
with open('backend/amr_api/urls.py', 'r') as f:
    content = f.read()

# Replace the function-based view with DRF class-based view
new_content = content.replace(
    "path('upload/csv', views.upload_csv, name='upload_csv'),",
    "path('upload/csv', views.CSVUploadView.as_view(), name='upload_csv'),"
)

# Write back
with open('backend/amr_api/urls.py', 'w') as f:
    f.write(new_content)

print("✅ Updated URLs to use DRF class-based view")
