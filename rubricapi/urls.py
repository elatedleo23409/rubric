from django.urls import path
from rubricapi import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
]