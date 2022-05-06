from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=250)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)

