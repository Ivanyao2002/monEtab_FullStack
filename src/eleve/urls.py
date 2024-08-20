from django.urls import path
from .views import index, ajouter, modifier

urlpatterns = [
    path('', index, name='liste_eleves'),
    path('ajouter-eleve', ajouter, name='ajouter_eleve'),
    path('modifier-eleve', modifier, name='modifier_eleve'),
] 