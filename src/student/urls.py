from django.urls import path
from .views import index_student, add_student, update_student, delete_student

app_name = 'student'

urlpatterns = [
    path('', index_student, name='index'),
    path('add-student', add_student, name='add'),
    path('update-student/<int:id>', update_student, name='update'),
    path('delete-student/<int:id>', delete_student, name='delete'),
    
] 