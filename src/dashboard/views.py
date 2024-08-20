from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    context = {
        'nom': 'Fuck',
        'prenom': 'Man'
    }

    return render(request, "dashboard/index.html", context) 


def rapport(request):

    context = {
        'nom': 'Fuck',
        'prenom': 'Man'
    }

    return render(request, "dashboard/rapport.html", context) 
