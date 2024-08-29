from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages

from .models import StudentModel
from .forms import StudentForm

# Create your views here.

def index_student(request):
    students_list =  StudentModel.objects.all()

    paginator = Paginator(students_list, 10)  
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    context = {
        'students': students
    }

    return render(request, "student/index.html", context) 

# def add_student(request):

#     if request.method == "POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             Student.objects.create(
#                 registration_number=form.cleaned_data['registration_number'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 birth_date=form.cleaned_data['birth_date'],
#                 city=form.cleaned_data['city'],
#                 phone=form.cleaned_data['phone'],
#                 classroom=form.cleaned_data['classroom']
#                 )
#             return redirect("student:index") 
#     else:
#         form = StudentForm()

#     return render(request, "student/add_student.html", {'form': form}) 


def add_student(request):
    context = {
        'title': 'Ajouter élève',
        'submit_value': 'Ajouter'
    }

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'élève a été ajouté avec succès.")
            return redirect("student:index")
        else:
            print('erreur')
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
    else:
        form = StudentForm()
    context['form'] = form

    return render(request, "student/add_student.html", context) 

def update_student(request, id):

    student = StudentModel.objects.get(id = id)
    context = {
        'title': 'Modifier le professeur',
        'submit_value': 'Modifier'
    }
    if request.method == "POST":
        student_form = StudentForm(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect("student:index")
        else:
            print("formulaire erroné")
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")


    student_form = StudentForm(instance=student)
    context['form'] = student_form

    return render(request, "student/add_student.html", context) 
 
def delete_student(request, id):
    student = get_object_or_404(StudentModel, id=id)
    student.delete()

    return redirect('student:index')
    