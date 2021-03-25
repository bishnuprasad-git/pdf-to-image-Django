from django.db import models

# Create your models here.
from django.db.models import IntegerField


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    date = models.DateField()
    query = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=60, default="")
    price = models.IntegerField()
    image = models.ImageField(upload_to='shop/images', default="")
    desc = models.CharField(max_length=500, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    order_id = models.IntegerField(default=9)
    total_amount = models.IntegerField(default=9)
    date = models.DateField()

    def __str__(self):
        return self.name


class Order_Update(models.Model):
    order_id = models.IntegerField(default=9)
    desc = models.CharField(max_length=300, default="Your order is on the way")
    date = models.DateField()

    def __str__(self):
        return self.desc
