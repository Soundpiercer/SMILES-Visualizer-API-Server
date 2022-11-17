from django.urls import path

from . import views


urlpatterns = [
    path('', views.generate_with_keyword), # localhost:8000/api/
]