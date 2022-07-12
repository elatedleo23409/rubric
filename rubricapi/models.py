from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.AutoField(primary_key=True)
    stuname = models.CharField(max_length=100)
    discovery = models.PositiveSmallIntegerField(blank=True, null=True)
    understanding = models.PositiveSmallIntegerField(blank=True, null=True)
    completion_of_tasks = models.PositiveSmallIntegerField(blank=True, null=True)
    interest = models.PositiveSmallIntegerField(blank=True, null=True)
    team_work = models.PositiveSmallIntegerField(blank=True, null=True)