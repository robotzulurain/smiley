from django.http import JsonResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import json

@csrf_exempt
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

# Keep the other functions as they are
def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return JsonResponse({
        "status": "healthy",
        "database": db_status,
        "service": "AMR Surveillance API"
    })

def options(request):
    return JsonResponse({})

def counts_summary(request):
    # Your existing implementation
    return JsonResponse({"summary": "data"})

def time_trends(request):
    # Your existing implementation
    return JsonResponse({"trends": "data"})

def antibiogram(request):
    # Your existing implementation
    return JsonResponse({"antibiogram": "data"})

def sex_age(request):
    # Your existing implementation
    return JsonResponse({"sex_age": "data"})

def facilities(request):
    # Your existing implementation
    return JsonResponse({"facilities": "data"})
