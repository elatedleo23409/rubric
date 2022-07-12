import imp
from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','stuname', 'discovery', 'understanding', 'completion_of_tasks', 'interest', 'team_work']
