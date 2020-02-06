from django.db import models

# Create your models here.

class Product(models.Model):
    #pid = models.IntegerField('prod_id')
    pname = models.CharField('prod_name', max_length=100)
    pprice = models.FloatField('prod_price')
    pqty = models.IntegerField('prod_qty')
    pcat = models.CharField('prod_cat', max_length=50)
    vendorref = models.ForeignKey('Vendor',models.CASCADE,related_name='products')

class Vendor(models.Model):
    pven = models.CharField('prod_ven', max_length=100)
    prew = models.CharField('prod_rew', max_length=100)

