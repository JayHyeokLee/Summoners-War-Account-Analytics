# upload/ai_views.py
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

@csrf_exempt
def get_ai_insight(request):
    if request.method == "POST":
        rune_data = json.loads(request.body)

        try:
            # Make request to OpenAI API
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {settings.OPENAI_API_KEY}"
                },
                json={
                    "model": "gpt-4",
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
            response_data = response.json()
            ai_response = response_data["choices"][0]["message"]["content"]
            return JsonResponse({"insight": ai_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=405)
