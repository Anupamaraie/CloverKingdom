from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    kingdom = models.CharField(max_length = 50)
    squad = models.CharField(max_length=100)
    help = models.TextField()
    
    def __str__(self):
        return self.name
    
class Regis(models.Model):
    fname=models.CharField(max_length = 100)
    lname=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    gen=models.CharField(max_length=100)
    cnumb=models.IntegerField()


    def __str__(self):
        return self.fname