from django.db import models

# Create your models here.

class Delivery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='delivery')


class Order(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
