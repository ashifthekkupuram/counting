from django.urls import path
from .views import HomeView,UpdateCount

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('update-count/', UpdateCount.as_view(), name='update-count')
]