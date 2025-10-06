from django.http import JsonResponse
from django.db import connection
import pandas as pd
import json

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
            "/api/summary/time-trends",
            "/api/summary/antibiogram",
            "/api/summary/sex-age",
            "/api/geo/facilities"
        ]
    })

def counts_summary(request):
    # Placeholder for counts summary endpoint
    return JsonResponse({
        "endpoint": "counts-summary",
        "status": "under_development",
        "message": "This endpoint will return AMR data counts summary",
        "data": {
            "total_records": 0,
            "total_patients": 0,
            "total_facilities": 0,
            "date_range": {"start": None, "end": None}
        }
    })

def time_trends(request):
    # Placeholder for time trends endpoint
    return JsonResponse({
        "endpoint": "time-trends",
        "status": "under_development",
        "message": "This endpoint will return AMR time trends data",
        "data": []
    })

def antibiogram(request):
    # Placeholder for antibiogram endpoint
    return JsonResponse({
        "endpoint": "antibiogram",
        "status": "under_development",
        "message": "This endpoint will return antibiogram data",
        "data": []
    })

def sex_age(request):
    # Placeholder for sex-age distribution endpoint
    return JsonResponse({
        "endpoint": "sex-age",
        "status": "under_development",
        "message": "This endpoint will return sex and age distribution data",
        "data": {"male": 0, "female": 0, "age_groups": []}
    })

def facilities(request):
    # Placeholder for facilities endpoint
    return JsonResponse({
        "endpoint": "facilities",
        "status": "under_development",
        "message": "This endpoint will return facility data",
        "data": []
    })

def upload_csv(request):
    if request.method == 'POST' and request.FILES.get('file'):
        csv_file = request.FILES['file']
        
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file)
            
            # Basic validation - check if it has required columns
            required_columns = ['organism', 'antibiotic', 'susceptibility']
            if not all(col in df.columns for col in required_columns):
                return JsonResponse({
                    'status': 'error',
                    'message': f'CSV must contain columns: {required_columns}'
                }, status=400)
            
            # Process the CSV data (placeholder - you can add your actual processing logic)
            record_count = len(df)
            
            return JsonResponse({
                'status': 'success',
                'message': f'CSV uploaded successfully. Processed {record_count} records.',
                'columns': list(df.columns),
                'sample_data': df.head(3).to_dict('records')  # First 3 rows as sample
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Error processing CSV: {str(e)}'
            }, status=400)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Please upload a CSV file using POST method'
    }, status=400)
