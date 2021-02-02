from django.db import models
from django.utils.translation import gettext_lazy as translate
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, last_name=last_name,
                            first_name=first_name)
        user.set_password(password)
        user.save()
        return user



class User(AbstractBaseUser):
    first_name = models.CharField(translate('Name'), max_length=30)
    last_name = models.CharField(translate('Lastname'), max_length=30)
    email = models.EmailField(translate('email address'), max_length=254, unique=True)
    password = models.CharField(max_length=35)

    
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

def __str__(self):
    return self.email

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    simptom1 = models.CharField(max_length=50)
    simptom2 = models.CharField(max_length=50)
    simptom3 = models.CharField(max_length=50)
    simptom4 = models.CharField(max_length=50)
    simptom5 = models.CharField(max_length=50)
    prediction = models.CharField(max_length=50)

     