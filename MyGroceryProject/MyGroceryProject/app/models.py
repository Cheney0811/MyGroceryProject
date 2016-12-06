"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.
class Product(models.Model):
    Product_Name = models.CharField(null = False, max_length = 10)

class Premium_User(models.Model):
    Premium_User_Name = models.CharField(null = False, max_length = 10, unique=True)
    Email = models.EmailField(null = False)
    Store_Name = models.CharField(null = False, max_length = 10)
    Store_Address = models.TextField(null = False)
    Store_Zip = models.CharField(null = False, max_length = 11)
    Store_Phone = models.CharField(null = False, max_length = 10)

class General_User(models.Model):
    General_User_Name = models.CharField(null = False, max_length = 10, unique=True)
    Email = models.EmailField(null = False)

class Product_List(models.Model):
    premium_user = models.ForeignKey(Premium_User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null = False)
    price = models.DecimalField(null = False, max_digits=5, decimal_places=2)

class Advertisement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mime_Type = models.CharField(max_length=128)
    time_of_post = models.TimeField(null = False)
    advertisement_concent = models.BinaryField()

class Advertisement_List(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    premium_user = models.ForeignKey(Premium_User, on_delete=models.CASCADE)
   