# Generated by Django 3.0.2 on 2020-01-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employees',
        ),
        migrations.AddField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(blank=True, help_text='The Employees that make up this Project', to='quickstart.Employee'),
        ),
    ]
