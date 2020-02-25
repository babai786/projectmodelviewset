from django.shortcuts import render

# Create your views here.

from testapp.serializers import  EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from testapp.models import Employee


class EmployeeCRUD(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


