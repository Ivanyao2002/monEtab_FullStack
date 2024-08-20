from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {
        'nom': 'Fuck',
        'prenom': 'Man'
    }

    return render(request, "professeur/index.html", context) 

def ajouter(request):

    context = {
        'nom': 'Fuck',
        'prenom': 'Man'
    }

    return render(request, "professeur/index.html", context) 

def modifier(request):

    context = {
        'nom': 'Fuck',
        'prenom': 'Man'
    }

    return render(request, "professeur/index.html", context) 
 