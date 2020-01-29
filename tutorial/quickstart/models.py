from django.db import models
from django.contrib.auth.models import Group, User


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='pics/', null=True, blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Project(models.Model):
    name = models.CharField(max_length=30)
    duration = models.CharField(default="Forever", max_length=30)
    is_active = models.BooleanField(default=True)
    employees = models.ManyToManyField(
        Employee,
        help_text="The Employees that make up this Project",
        blank=True
    )

    def __str(self):
        return str(self.name)
