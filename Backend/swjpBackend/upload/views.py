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
        energy_runes, guard_runes, swift_runes, blade_runes, rage_runes, focus_runes, endure_runes, fatal_runes, despair_runes, vampire_runes, violent_runes, nemesis_runes, will_runes, shield_runes, revenge_runes, destroy_runes, fight_runes, determination_runes, enhance_runes, accuracy_runes, tolerance_runes, seal_runes, intangible_runes = []
        
        for rune in sorted_runes_all:
            match sorted_runes_all["sets"]:
                case 1:
                    energy_runes.append(rune)
                case 2:
                    guard_runes.append(rune)
                case 3:
                    swift_runes.append(rune)
                case 4:
                    blade_runes.append(rune)
                case 5:
                    rage_runes.append(rune)
                case 6:
                    focus_runes.append(rune)
                case 7:
                    endure_runes.append(rune)
                case 8:
                    fatal_runes.append(rune)
                case 10:
                    despair_runes.append(rune)
                case 11:
                    vampire_runes.append(rune)
                case 13:
                    violent_runes.append(rune)
                case 14:
                    nemesis_runes.append(rune)
                case 15:
                    will_runes.append(rune)
                case 16:
                    shield_runes.append(rune)
                case 17:
                    revenge_runes.append(rune)
                case 18:
                    destroy_runes.append(rune)
                case 19:
                    fight_runes.append(rune)
                case 20:
                    determination_runes.append(rune)
                case 21:
                    enhance_runes.append(rune)
                case 22:
                    accuracy_runes.append(rune)
                case 23:
                    tolerance_runes.append(rune)
                case 24:
                    seal_runes.append(rune)
                case 25:
                    intangible_runes.append(rune)

        return Response(sorted_runes_all,energy_runes, guard_runes, swift_runes, blade_runes, rage_runes, focus_runes, endure_runes, fatal_runes, despair_runes, vampire_runes, violent_runes, nemesis_runes, will_runes, shield_runes, revenge_runes, destroy_runes, fight_runes, determination_runes, enhance_runes, accuracy_runes, tolerance_runes, seal_runes, intangible_runes, status=200)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON file'}, status=400)
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return Response({"error": str(e)}, status=500)

