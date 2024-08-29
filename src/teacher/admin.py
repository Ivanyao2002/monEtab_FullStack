from django.contrib import admin

from .models import TeacherModel

# Register your models here.

@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_vacant', 'subject_taught', 'birth_date')
    
    list_filter = ('id', 'first_name')
    
    search_fields = ('first_name', 'last_name', 'subject_taught')

