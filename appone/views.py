from django.shortcuts import render
from appone.models import Employee,Address
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from appone.empserializer import EmpSer,AddressSer

class AddressOperations(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSer

class EmpOperations(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class =EmpSer