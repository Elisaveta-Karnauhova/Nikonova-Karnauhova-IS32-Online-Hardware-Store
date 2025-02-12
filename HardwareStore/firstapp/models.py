from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     manufacturer = models.CharField(max_length=50)
#     color = models.CharField(max_length=50)
#     price = models.CharField(max_length=100)
#     available = models.CharField(max_length=50) 
#     amount = models.IntegerField(default=0)
    

    

class Product(models.Model):
    name = models.CharField(max_length=50, default=0)
    manufacturer_id = models.IntegerField(default=0)
    category = models.CharField(max_length=50, default=0)
    color = models.CharField(max_length=50, default=0)
    price =  models.IntegerField(default=0)
    

class Customer(models.Model):
    name = models.CharField(max_length=50, default=0)
    surname = models.CharField(max_length=50, default=0)
    
   
class Manufacturer(models.Model):
    name = models.CharField(max_length=200, default=0)


class Purchase_item(models.Model):
    product_id = models.IntegerField(default=0)
    product_count = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    customer_id = models.IntegerField(default=0)
    