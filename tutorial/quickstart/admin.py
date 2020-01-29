from django.contrib import admin
from .models import Employee, Project

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ordering = ("-id",)

    list_display = ("id", "first_name", "last_name")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ordering = ("-id",)

    list_display = ("id", "name", "duration", "is_active")