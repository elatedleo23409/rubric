# Generated by Django 4.0.6 on 2022-07-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.AutoField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=100)),
                ('discovery', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
