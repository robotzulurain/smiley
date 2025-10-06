from django.http import JsonResponse
from django.db import connection

def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"
    
    return JsonResponse({
        "status": "healthy",
        "database": db_status,
        "service": "AMR Surveillance API"
    })

def options(request):
    return JsonResponse({
        "message": "AMR API is working!",
        "endpoints": [
            "/api/health/",
            "/api/options/",
            "/api/summary/counts-summary",
            "/api/summary/time-trends"
        ]
    })
