from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    message = models.CharField(max_length=1000) 


    
