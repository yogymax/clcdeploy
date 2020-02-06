from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from apptwo.models import Product,Vendor


class ProdSer(ModelSerializer):
    #vendorref = VendorSer()
    class Meta:
        model = Product
        fields = '__all__'


class VendorSer(ModelSerializer):
    #products = ProdSer(many=True)
    class Meta:
        model = Vendor
        fields = '__all__'
        #exclude = ('id',)
