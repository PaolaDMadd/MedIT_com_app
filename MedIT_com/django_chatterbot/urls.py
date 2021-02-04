from django.conf.urls import url
from django.contrib import admin
from django_chatterbot.views import get_response

urlpatterns = [
    url('api/chatbot', get_response)
]