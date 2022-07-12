# Generated by Django 4.0.6 on 2022-07-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rubricapi', '0002_student_completion_of_tasks_student_interest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='completion_of_tasks',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='discovery',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='interest',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='team_work',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='understanding',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
