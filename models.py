from django.db import models
from django.contrib import auth
from django.db.models import ImageField
from datetime import datetime


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def cat_name(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    photo = models.ImageField(upload_to='products/product_photo', null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name


class Basket(models.Model):
    auth_user = models.ForeignKey(auth.models.User)
    product = models.ForeignKey(Products)
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.auth_user.username
