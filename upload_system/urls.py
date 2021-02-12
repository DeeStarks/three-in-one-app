from django.urls import path
from .views import upload_system

urlpatterns = [
    path('upload-system/', upload_system, name="upload")
]