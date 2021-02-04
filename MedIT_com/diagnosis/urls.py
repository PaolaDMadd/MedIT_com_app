from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name='profile'),
    path('diagnosis', views.index, name='diagnosis'),
    path('history', views.history, name='history')
]