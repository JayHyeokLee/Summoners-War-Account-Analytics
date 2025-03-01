import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

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
                            "content": "You are an expert in Summoners War rune efficiency analysis."
                        },
                        {
                            "role": "user",
                            "content": f"Analyze the following rune data and provide insights: {json.dumps(rune_data)}"
                        }
                    ]
                }
            )
            # Debug
            print("OpenAI Response Status:", response.status_code)
            print("OpenAI Response Data:", response.json())

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