from django.urls import path
from .views import index, ajouter, modifier

urlpatterns = [
    path('', index, name='liste_utilisateurs'),
    path('ajouter-utilisateur', ajouter, name='ajouter_utilisateur'),
    path('modifier-utilisateur', modifier, name='modifier_utilisateur'),
] 