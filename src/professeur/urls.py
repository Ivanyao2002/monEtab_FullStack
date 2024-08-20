from django.urls import path
from .views import index, ajouter, modifier

urlpatterns = [
    path('', index, name='liste_professeurs'),
    path('ajouter-professeur', ajouter, name='ajouter_professeur'),
    path('modifier-professeur', modifier, name='modifier_professeur'),
] 