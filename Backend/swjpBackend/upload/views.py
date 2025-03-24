from django.shortcuts import render
import json
import statistics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .process_runes import calculate_efficiency
from .models import UserAVG

@api_view(['POST'])
def upload_json(request):
    #Getting upload file
    file = request.FILES.get('file')

    if not file:
        return Response({'error': 'No file uploaded'}, status=400)
    
    try:
        #loading and parsing json
        data = json.load(file)
        user_id = data["wizard_info"["wizard_id"]]
        user_name = data["wizard_info"["wizard_name"]]
        runes = data["runes"]

        rune_efficiencies = [calculate_efficiency(rune) for rune in runes]
        sorted_runes_all = sorted(rune_efficiencies, key=lambda r:r["current_efficiency"], reverse=True)
        sorted_runes_swift = []
        sorted_runes_vio = []
        sorted_runes_will = []
        sorted_runes_despair = []
        sorted_runes_seal = []

        for rune in sorted_runes_all:
            if rune["rune_set"] == 3:
                if len(sorted_runes_swift) >= 100:
                    continue
                else:
                    sorted_runes_swift.append(rune["current_efficiency"])
            elif rune["rune_set"] == 10:
                if len(sorted_runes_despair) >= 100:
                    continue
                else:
                    sorted_runes_despair.append(rune["current_efficiency"])
            elif rune["rune_set"] == 13:
                if len(sorted_runes_vio) >= 100:
                    continue
                else:
                    sorted_runes_vio.append(rune["current_efficiency"])
            elif rune["rune_set"] == 15:
                if len(sorted_runes_will) >= 100:
                    continue
                else:
                    sorted_runes_will.append(rune["current_efficiency"])
            elif rune["rune_set"] == 24:
                if len(sorted_runes_seal) >= 100:
                    continue
                else:
                    sorted_runes_seal.append(rune["current_efficiency"])
        
        global_avg = statistics.mean(sorted_runes_all[:500])
        swift_avg = statistics.mean(sorted_runes_swift)
        vio_avg = statistics.mean(sorted_runes_vio)
        will_avg = statistics.mean(sorted_runes_will)
        despair_avg = statistics.mean(sorted_runes_despair)
        seal_avg = statistics.mean(sorted_runes_seal)

        user = UserAVG(userID=user_id, userName=user_name, globalAVG=global_avg, vioAVG=vio_avg, willAVG=will_avg, swiftAVG=swift_avg, desAVG=despair_avg, sealAVG=seal_avg)
        user.save()
        
        return Response(sorted_runes_all, status=200)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON file'}, status=400)
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return Response({"error": str(e)}, status=500)

