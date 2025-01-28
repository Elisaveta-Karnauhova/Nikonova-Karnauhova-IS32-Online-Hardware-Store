from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    