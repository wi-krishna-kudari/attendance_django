from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.IntegerField(unique=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=['active', 'inactive'])
    age = models.IntegerField(default=18)
