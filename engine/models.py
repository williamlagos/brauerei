from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)
    photo = models.ImageField()
    phone = models.CharField(max_length=64)
    side = models.IntegerField()
    rank = models.IntegerField()

class Product(models.Model):
    sku = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField()

class Stock(models.Model):
    key = models.ForeignKey(Product)
    provider = models.ForeignKey(User)
    value = models.FloatField()
    quantity = models.IntegerField()

class Request(models.Model):
    client = models.ForeignKey(User)
    # provider = models.ForeignKey(User)
    products = models.ManyToManyField(Product)
    estimated = models.DateTimeField()
