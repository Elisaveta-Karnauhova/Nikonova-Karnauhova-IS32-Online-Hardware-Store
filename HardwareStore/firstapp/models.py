from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    available = models.CharField(max_length=50) 
    amount = models.IntegerField(default=0)
    