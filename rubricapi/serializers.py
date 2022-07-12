from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['rollno','stuname', 'discovery', 'understanding', 'completion_of_tasks', 'interest', 'team_work']