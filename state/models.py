from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True) 

class States(models.Model):
    State = models.CharField(max_length=250)
    Capital = models.CharField(max_length=250)
    #phanthonbuster
    Population = models.CharField(max_length=250)
    
