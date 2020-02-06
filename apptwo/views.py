from django.shortcuts import render
from apptwo.models import Product,Vendor
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from apptwo.productserialier import ProdSer,VendorSer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,DestroyModelMixin

#class CustomeViewSet(CreateModelMixin,ListModelMixin,DestroyModelMixin,GenericViewSet):
 #   pass

from rest_framework.permissions import AllowAny,IsAdminUser,BasePermission
class MyOwnPermissions(BasePermission):

    def has_permission(self, request, view):
        print('inside has permission')
        if bool(request.user and request.user.is_authenticated) and request.data['pven'] in ('flipkart','amazon','snapdeal'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        print('inside has object permission')
        print(request.data)
        print(view)
        print(obj)
        return True




class VendorOperations(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Vendor.objects.all()
    serializer_class =VendorSer

    def get_permissions(self):
        if self.action=="create":
            self.permission_classes = (MyOwnPermissions,)
        return super().get_permissions()


from rest_framework.response import Response

'''
"pname": "string",
  "pprice": 0,
  "pqty": 0,
  "pcat": "string",
'''

def validateproductinfo(prod):
    errors = {}
    if len(prod['pname'])<3:
        errors['name'] = "Invalid Product Name"
    if float(prod['pprice'])<100:
        errors['price'] = "Invalid Product Price"
    if int(prod['pqty']) < 10:
        errors['price'] = "Less Quantities"

    return errors

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
class ProductOperations(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class =ProdSer

    @action(detail=False,methods=['GET'])
    def get_all_product_prices(self,request,*args,**kwargs):
        sum = 0.0
        products=  Product.objects.all()
        for item in products:
            sum += item.pprice
        return Response({"totalprice" : str(sum)})

    def create(self, request, *args, **kwargs):
        prodinfo = request.data
        errors = validateproductinfo(prodinfo)
        if errors:
            return Response(errors)
        else:
            return super().create(request)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.pcat='DELETED'
            instance.save()
            return Response({"status" :"Record Removed..!"})
        else:
            return Response({"detail": "Not found..!"})

