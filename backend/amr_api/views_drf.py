from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd

class CSVUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({
                'status': 'error',
                'message': 'No file provided'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        csv_file = request.FILES['file']
        
        try:
            # Read the CSV file
            df = pd.read_csv(csv_file)
            
            # Basic validation - check if it has required columns
            required_columns = ['organism', 'antibiotic', 'susceptibility']
            if not all(col in df.columns for col in required_columns):
                return Response({
                    'status': 'error',
                    'message': f'CSV must contain columns: {required_columns}'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Process the CSV data
            record_count = len(df)
            
            return Response({
                'status': 'success',
                'message': f'CSV uploaded successfully. Processed {record_count} records.',
                'columns': list(df.columns),
                'sample_data': df.head(3).to_dict('records')
            })
            
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error processing CSV: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)

