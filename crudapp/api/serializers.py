from django.db.models import fields
from crudapp.models import EmployeeDetails
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeDetails
        fields=['id', 'emp_name', 'emp_email', 'emp_password']