"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Product(models.Model):
    Product_ID = models.IntegerField(primary_key = True)
    Product_Name = models.CharField(null = False, max_length = 10)

class Premium_User(models.Model):
    Premium_User_ID = models.IntegerField(primary_key = True)
    Premium_User_Name = models.CharField(null = False, max_length = 10)
    Premium_User_Password = models.CharField(null = False, max_length = 20)
    Email = models.EmailField(null = False)
    Address = models.TextField(null = False)
    Zip = models.CharField(null = False, max_length = 11)
    Phone = models.CharField(null = False, max_length = 10)

class General_User(models.Model):
    General_User_ID = models.IntegerField(primary_key = True)
    General_User_Name = models.CharField(null = False, max_length = 10)
    General_User_Password = models.CharField(null = False, max_length = 20)
    Email = models.EmailField(null = False)

class Product_List(models.Model):
    Premium_User_ID = models.ForeignKey(Premium_User)
    Product_ID = models.ForeignKey(Product)
    Quantity = models.IntegerField(null = False)
    Price = models.DecimalField(null = False, max_digits=5, decimal_places=2)
    unique_together = ("Premium_User_ID","Product_ID")

class Advertisement(models.Model):
    Product_ID = models.ForeignKey(Product)
    Premium_User_ID = models.ForeignKey(Premium_User)
    Time_Of_Post = models.TimeField(null = False)
    Date_Of_Start = models.DateTimeField(null = False)
    Date_Of_End = models.DateTimeField(null = False)
    Advertisement_Concent = models.TextField
    unique_together = ("Product_ID","Premium_User_ID","Time_Of_Post")

class Advertisement_List(models.Model):
    Product_ID = models.ForeignKey(Product)
    Premium_User_ID = models.ForeignKey(Premium_User)
    Receiver_ID = models.IntegerField(General_User)
    Time_Of_Post = models.TimeField(null = False)
   
    unique_together = ("Product_ID","Premium_User_ID","Receiver_ID","Time_Of_Post")