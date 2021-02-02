from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['email', 'password']