from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.decorators import Response

@api_view(['POST'])
def upload_json(request):
    #Getting upload file
    file = request.FILES.get('file')

    if not file:
        return Response({'error': 'No file uploaded'}, status=400)
    
    try:
        #loading and parsing json
        data = json.load(file)
        runes = data["runes"]

        #need to insert processing logic here

        return Response({'message': 'File uploaded successfully'})
    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON file'}, status=400)

