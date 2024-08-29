from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages

from .models import TeacherModel
from .forms import TeacherForm

# Create your views here.

def index_teacher(request):

    teacher_list =  TeacherModel.objects.all()

    paginator = Paginator(teacher_list, 10)  
    page_number = request.GET.get('page')
    teachers = paginator.get_page(page_number)

    context = {
        'teachers': teachers
    }
    return render(request, "teacher/index.html", context) 

# def add_teacher(request):
#     forms = TeacherForm()

#     if request.method == "POST":
#         form = TeacherForm(request.POST)
#         if form.is_valid():
#             Teacher.objects.create(
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 birth_date=form.cleaned_data['birth_date'],
#                 city=form.cleaned_data['city'],
#                 phone=form.cleaned_data['phone'],
#                 subject_taught=form.cleaned_data['subject_taught'],
#                 next_class=form.cleaned_data['next_class'],
#                 next_meeting_topic=form.cleaned_data['next_meeting_topic'],
#                 is_vacant=form.cleaned_data['is_vacant']
#                 )
#             return redirect("teacher:index") 
#     else:
#         form = TeacherForm()

#     context = {
        
#     }

#     return render(request, "teacher/add_teacher.html", {'form': form, 'forms': forms}) 


def add_teacher(request):
    context = {
        'title': 'Ajouter professeur',
        'submit_value': 'Ajouter'
    }

    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le professeur a été ajouté avec succès.")
            return redirect("teacher:index")
        else:
            print('erreur')
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
    else:
        form = TeacherForm()
    context['form'] = form

    return render(request, "teacher/add_teacher.html", context) 
 

def update_teacher(request, id):

    teacher = TeacherModel.objects.get(id = id)
    context = {
        'title': 'Modifier le professeur',
        'submit_value': 'Modifier'
    }
    if request.method == "POST":
        teacher_form = TeacherForm(request.POST, instance=teacher)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect("teacher:index")
        else:
            print("formulaire erroné")
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    teacher_form = TeacherForm(instance=teacher)
    context['form'] = teacher_form

    return render(request, "teacher/add_teacher.html", context) 
 
def delete_teacher(request, id):
    teacher = get_object_or_404(TeacherModel, id=id)
    teacher.delete()

    return redirect('teacher:index') 