from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from .forms import UserForm
from .models import UserModel

# Create your views here.

def index_user(request):
    user_list =  UserModel.objects.all()

    paginator = Paginator(user_list, 10)  
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)

    context = {
        'users': users
    }
    return render(request, "user/index.html", context) 

# def add(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             User.objects.create(
#                 pseudo=form.cleaned_data['pseudo'],
#                 password=make_password(form.cleaned_data['password'])
#                 )
#             return redirect("user:index")
#     else:
#         form = UserForm()

#     return render(request, "user/add_user.html", {'form': form}) 

def add_user(request):
    context = {
        'title': 'Ajouter utilisateur',
        'submit_value': 'Ajouter'
    }

    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password']) 
            user_form.save()
            messages.success(request, "L'utilisateur a été ajouté avec succès.")
            return redirect("user:index")
        else:
            print("formulaire erroné")
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
            

    user_form = UserForm()
    context['form'] = user_form

    return render(request, "user/add_user.html", context)

def update_user(request, id):
    user = UserModel.objects.get(id = id)
    context = {
        'title': 'Modifier l\'utilisateur',
        'submit_value': 'Modifier'
    }
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():    
            user = user_form.save(commit=False)
            user.password = make_password(user_form.cleaned_data['password']) 
            user_form.save()
            messages.success(request, "L'utilisateur a été ajouté avec succès.")
            return redirect("user:index")
        else:
            print("formulaire erroné")
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    user_form = UserForm(instance=user)
    context['form'] = user_form

    return render(request, "user/add_user.html", context) 

def delete_user(request, id):
    user = get_object_or_404(UserModel, id=id)
    user.delete()
    messages.success(request, "L'utilisateur a été supprimé avec succès.")  
    return redirect('user:index')

def login(request):

    return render(request, "login.html")   
 