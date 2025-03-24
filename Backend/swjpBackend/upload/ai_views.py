import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

RUNE_MAPPING = {
    1: 'Energy',
    2: 'Guard',
    3: 'Swift',
    4: 'Blade',
    5: 'Rage',
    6: 'Focus',
    7: 'Endure',
    8: 'Fatal',
    10: 'Despair',
    11: 'Vampire',
    13: 'Violent',
    14: 'Nemesis',
    15: 'Will',
    16: 'Shield',
    17: 'Revenge',
    18: 'Destroy',
    19: 'Fight',
    20: 'Determination',
    21: 'Enhance',
    22: 'Accuracy',
    23: 'Tolerance',
    24: 'Seal',
    25: 'Intangible'
}

THEORETICAL_MAX = 144

POINT_CUTOFF_ARENA ={
    "Challenger_1": 950,
    "Challenger_2": 1000,
    "Challenger_3": 1050,
    "Fighter_1": 1100,
    "Fighter_2": 1200,
    "Fighter_3": 1300,
    "Conqueror_1": 1400,
    "Conqueror_2": 1400,
    "Conqueror_3": 1400,
    "Punisher_1": 1500,
    "Punisher_2": 1500,
    "Punisher_3": 1500,
    "Guardian_1": 1600,
    "Guardian_2": 1600,
    "Guardian_3": 1600,
    "Legend": 1600,
}

POPULATION_CUTOFF_ARENA ={
    "Conqueror_1": 10000,
    "Conqueror_2": 3000,
    "Conqueror_3": 1500,
    "Punisher_1": 1000,
    "Punisher_2": 750,
    "Punisher_3": 500,
    "Guardian_1": 300,
    "Guardian_2": 100,
    "Guardian_3": 30,
    "Legend": 1,
}

POINT_CUTOFF_RTA ={
    "Challenger_1": 950,
    "Challenger_2": 1000,
    "Challenger_3": 1050,
    "Fighter_1": 1100,
    "Fighter_2": 1150,
    "Fighter_3": 1200,
    "Conqueror_1": 1300,
    "Conqueror_2": 1400,
    "Conqueror_3": 1500,
    "Punisher_1": 1600,
    "Punisher_2": 1600,
    "Punisher_3": 1600,
    "Guardian_1": 1700,
    "Guardian_2": 1800,
    "Guardian_3": 1900,
}

POPULATION_CUTOFF_RTA ={
    "Conqueror_1": 60000,
    "Conqueror_2": 30000,
    "Conqueror_3": 15000,
    "Punisher_1": 10000,
    "Punisher_2": 7500,
    "Punisher_3": 5000,
    "Guardian_1": 3000,
    "Guardian_2": 1000,
    "Guardian_3": 300,
}

@csrf_exempt
def get_ai_insight(request):
    if request.method == "POST":
        rune_data = json.loads(request.body)

        #Debug
        #print("Received Rune Data:", rune_data)

        try:
            # Make request to OpenAI API
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "You are an expert in Summoners War rune efficiency analysis."
                                "Analyze the following rune data using the given mappings, "
                                "theoretical max efficiency, and rank cutoffs."
                            )
                        },
                        {
                            "role": "user",
                            "content": (
                                f"Rune mappings: {json.dumps(RUNE_MAPPING)}\n"
                                f"Theoretical Max Efficiency: {THEORETICAL_MAX}\n"
                                f"Rank Cutoffs: {json.dumps(POINT_CUTOFF_RTA, POPULATION_CUTOFF_RTA)}\n"
                                "There are around 250000 players playing RTA, each win and loss changes your points by 10 to 15 points,\n"
                                "Population cutoff means that only those amounts of players can be that rank or higher,\n"
                                "You need around 40 high score violent runes, 12-16 high score swift runes, 12-16 high score despair runes and 20-24 high score will runes.\n"
                                "Given the information, provide analysis for:\n"
                                "- The average efficiency for the top 100 runes of violent, will, despair, swift\n"
                                "- Which sets need the most improvement among the 4 listed but also quickly mention some of the other sets\n"
                                "- Approximate rank based on efficiency\n"
                                f"Analyze the following rune data and provide insights: {json.dumps(rune_data)}"

                            )
                        }
                    ]
                }
            )

            # Handle response
            if response.status_code == 200:
                
                formatted_response = ai_response.replace("- ", "\n- ")

                ai_response = response.json()["choices"][0]["message"]["content"]
                return JsonResponse({"insight": ai_response})
            else:
                return JsonResponse({"error": "Failed to get response from OpenAI"}, status=500)
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", e)
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except KeyError as e:
            print("Key Error:", e)
            return JsonResponse({"error": f"Missing key: {str(e)}"}, status=500)
        except Exception as e:
            print("Unexpected Error:", e)
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)