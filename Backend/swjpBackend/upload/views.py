from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .process_runes import calculate_efficiency

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

        rune_efficiencies = [calculate_efficiency(rune) for rune in runes]

        #print("done processing: ", rune_efficiencies)

        sorted_runes_all = sorted(rune_efficiencies, key=lambda r:r["current_efficiency"], reverse=True)
        
        return Response(sorted_runes_all, status=200)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON file'}, status=400)
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return Response({"error": str(e)}, status=500)

