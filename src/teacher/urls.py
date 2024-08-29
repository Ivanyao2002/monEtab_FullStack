from django.urls import path
from .views import index_teacher, add_teacher, update_teacher, delete_teacher

app_name = 'teacher'

urlpatterns = [
    path('', index_teacher, name='index'),
    path('add-teacher', add_teacher, name='add'),
    path('update-teacher/<int:id>', update_teacher, name='update'),
    path('delete-teacher/<int:id>', delete_teacher, name='delete'),
] 