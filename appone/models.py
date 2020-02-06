from django.db import models

# Create your models here.


class Employee(models.Model):
    ename = models.CharField('emp_name',max_length=100)
    esal = models.FloatField('emp_sal')
    eage = models.IntegerField('emp_age')
    epos = models.CharField('emp_pos',max_length=50)
    ecomp = models.CharField('emp_cmp', max_length=100)
    addressref = models.ForeignKey('Address',models.CASCADE)

class Address(models.Model):
    pincode = models.IntegerField('pincode')
    city = models.CharField('adr_city', max_length=100)


