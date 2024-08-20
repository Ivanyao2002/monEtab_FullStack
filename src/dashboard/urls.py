from django.urls import path
from .views import index, rapport

urlpatterns = [
    path('', index, name='dashboard'),
    path('rapport/', rapport, name='rapport'),
] 