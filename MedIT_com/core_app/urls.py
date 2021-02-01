from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login', views.login, name='login'), 
    path('register', views.register, name='register'),
    path('profile<int:id>', views.profile, name='profile') # to accept only numbers as id param
]