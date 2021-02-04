from django.conf.urls import url
from django.contrib import admin
from django_chatterbot.views import get_response

urlpatterns = [
    url('chatbot/', get_response, name='chatbot')
]