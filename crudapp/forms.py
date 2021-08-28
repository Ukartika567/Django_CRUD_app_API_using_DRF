from django import forms
from django.db import models
from django.db.models.query import QuerySet
from django.forms import fields, widgets
from crudapp.models import EmployeeDetails

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeDetails
        fields="__all__"
        widgets={

        'emp_name':forms.TextInput(attrs={'class':'form-control'}),
        'emp_email':forms.EmailInput(attrs={'class':'form-control'}),
        'emp_password':forms.PasswordInput(attrs={'class':'form-control'}),
                
        }
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        
