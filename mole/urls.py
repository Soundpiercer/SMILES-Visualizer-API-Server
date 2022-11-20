from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("", views.MolecularList.as_view(), name="molecular_list"),
    path("<int:pk>/", views.MolecularDetail.as_view(), name="molecular_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
