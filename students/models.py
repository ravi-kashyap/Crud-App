from django.db import models

# Create your models here.

class student(models.Model):
    name =  models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    email =  models.CharField(max_length=50)
    phone =  models.CharField(max_length=10)
    roll =  models.CharField(max_length=50)
    address = models.CharField(max_length=250)
