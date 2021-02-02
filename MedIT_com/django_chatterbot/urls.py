from django.conf.urls import url
from django.contrib import admin

from django_chatterbot.api import ChatterBotAppView

urlpatterns = [
    url('chat/', ChatterBotAppView.as_view(), name='chatbot')
]