from django.contrib import admin
from .models import EmployeeDetails
# Register your models here.

@admin.register(EmployeeDetails)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id', 'emp_name', 'emp_email', 'emp_password']
