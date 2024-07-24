from django.db import models
from django.urls import reverse
# Create your models here.

class Usersdetails(models.Model):
    username = models.CharField(max_length=100)
    #lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    #state = models.CharField(max_length=100)

    def __str__(self):
        return self.username




class Usertaste(models.Model):
    emailid = models.ForeignKey(Usersdetails,on_delete=models.CASCADE)
    taste = models.CharField(max_length=50)



