from django.db import models

# Create your models here.
class SmallDogs(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    age = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/")

class LargeDogs(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    age = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/")

