from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_email=models.EmailField(max_length=100)
    emp_password=models.CharField(max_length=100)
    
    
