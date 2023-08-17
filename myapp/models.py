from django.db import models
from django.conf import settings

# Create your models here.
class Account(models.Model):
    First_Name = models.CharField(max_length = 64 )
    Last_Name = models.CharField(max_length = 64)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 100)
    rank = models.CharField(max_length = 20)