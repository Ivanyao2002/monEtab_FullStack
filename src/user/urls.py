from django.urls import path
from .views import index_user, add_user, update_user, delete_user

app_name = 'user'

urlpatterns = [
    path('', index_user, name='index'),
    path('add-user', add_user, name='add'),
    path('update-user/<int:id>', update_user, name='update'),
    path('delete-user/<int:id>', delete_user, name='delete'),
] 