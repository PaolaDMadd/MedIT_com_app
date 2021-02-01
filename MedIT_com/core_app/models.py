from django.db import models


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=35)

def __str__(self):
    return self.first_name

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    simptom1 = models.CharField(max_length=50)
    simptom2 = models.CharField(max_length=50)
    simptom3 = models.CharField(max_length=50)
    simptom4 = models.CharField(max_length=50)
    simptom5 = models.CharField(max_length=50)
    prediction =models.TextField()

     