from django.conf.urls import url
from django.contrib import admin

from django_chatterbot.views import ChatterBotAppView, ChatterBotApiView

urlpatterns = [
    url('chatbot/', ChatterBotAppView.as_view(), name='main'),
    url('api/chatbot/', ChatterBotAppView.as_view(), name='chatbot-api')
]