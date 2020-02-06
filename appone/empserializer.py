from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from appone.models import Employee,Address

class EmpSer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AddressSer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'