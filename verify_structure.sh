#!/bin/bash
echo "=== Project Structure Verification ==="
echo "Current directory: $(pwd)"
echo ""
echo "Key files:"
[ -f "requirements.txt" ] && echo "✅ requirements.txt" || echo "❌ requirements.txt"
[ -f "render.yaml" ] && echo "✅ render.yaml" || echo "❌ render.yaml" 
[ -f "build.sh" ] && echo "✅ build.sh" || echo "❌ build.sh"
[ -f "startup.sh" ] && echo "✅ startup.sh" || echo "❌ startup.sh"
[ -f "manage.py" ] && echo "✅ manage.py (root)" || echo "❌ manage.py (root)"
[ -f "backend/manage.py" ] && echo "✅ backend/manage.py" || echo "❌ backend/manage.py"
[ -f "backend/amr_project/settings_production.py" ] && echo "✅ backend/amr_project/settings_production.py" || echo "❌ backend/amr_project/settings_production.py"

echo ""
echo "Python version in render.yaml:"
grep "PYTHON_VERSION" render.yaml
