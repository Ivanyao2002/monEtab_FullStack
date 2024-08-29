from django.contrib import admin

from .models import StudentModel

# Register your models here.

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'registration_number', 'classroom', 'birth_date')
    
    list_filter = ('id', 'first_name')
    
    search_fields = ('first_name', 'last_name', 'registration_number')
