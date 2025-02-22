from django.urls import path
from .views import upload_json
from .ai_views import get_ai_insight

urlpatterns = [
    path("upload/", upload_json, name="upload_json"),
    path('ai-insight/', get_ai_insight, name='ai-insight'),
]
