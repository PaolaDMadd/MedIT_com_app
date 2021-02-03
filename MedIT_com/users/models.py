from django.db import models
from django.contrib.auth.models import User

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    simptom1 = models.CharField(max_length=50)
    simptom2 = models.CharField(max_length=50)
    simptom3 = models.CharField(max_length=50)
    simptom4 = models.CharField(max_length=50)
    simptom5 = models.CharField(max_length=50)
    prediction =models.TextField()

     