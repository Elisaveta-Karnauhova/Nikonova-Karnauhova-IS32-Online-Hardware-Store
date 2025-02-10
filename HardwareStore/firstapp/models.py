from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    available = models.CharField(max_length=50) 
    amount = models.IntegerField(default=0)
    

    

# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     manufacturer_id = models.IntegerField()
#     category_id = models.IntegerField()
#     color = models.CharField(max_length=50)
#     price = models.CharField(max_length=100)
    

# class Customer(models.Model):
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
    
   
# class Manufacturer(models.Model):
#     name = models.CharField(max_length=200)

# class Category(models.Model):
#     name = models.CharField(max_length=200)

# class Purchase_item(models.Model):
#     product_id = models.IntegerField()
#     product_count = models.IntegerField()
#     product_price = models.IntegerField()
#     customer_id = models.IntegerField()

    