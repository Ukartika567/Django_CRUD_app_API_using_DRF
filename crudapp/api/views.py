from crudapp.models import EmployeeDetails
from rest_framework import viewsets
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeSerializer