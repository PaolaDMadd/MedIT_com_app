from django.conf.urls import url
from django.contrib import admin

from django_chatterbot.views import  ChatterBotApiView

urlpatterns = [
    # url('chatbot/', ChatterBotAppView.as_view(), name='main'),
    url('api/chatbot/', ChatterBotApiView.as_view(), name='chatbot-api')
]