from django.urls import path
from .views import HomeView, DetailView, CompareView, SavedListView, save_to_list
from django.contrib.auth.decorators import login_required

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<str:id>', DetailView.as_view(), name='detail'),
    path('compare', CompareView.as_view(), name='compare'),
    path('compare/<str:id1>/<str:id2>', CompareView.as_view(), name='compare'),
    path('save-to-list/<str:formula>', save_to_list, name='save-to-list'),
    path('saved-list', login_required(SavedListView.as_view()), name='saved-list')
]
