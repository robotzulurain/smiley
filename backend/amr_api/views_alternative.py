from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import json

@method_decorator(csrf_exempt, name='dispatch')
class UploadCSVView(View):
    def post(self, request):
        if request.FILES.get('file'):
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
                
                # Process the CSV data
                record_count = len(df)
                
                return JsonResponse({
                    'status': 'success',
                    'message': f'CSV uploaded successfully. Processed {record_count} records.',
                    'columns': list(df.columns),
                    'sample_data': df.head(3).to_dict('records')
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

# Keep other functions as is
