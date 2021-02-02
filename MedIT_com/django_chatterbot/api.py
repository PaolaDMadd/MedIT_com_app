from django.shortcuts import render
import json
# from django.views.generic.base import TemplateView
from django.views.generic import View 
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.ext.django_chatterbot import settings

chatterbot = ChatBot('MediBot')

trainer = ListTrainer(chatterbot)

trainer.train([
    'Test 1',
    'Returning test 1'
])

# Create your views here.

class ChatterBotAppView(View):
    """ Provide an API endpoint to interact with ChatBot"""

    def get(self, request, *args, **kwargs):
        """Return data corresponding to the current conversation"""

        # return JsonResponse({
        #     'name': self.chatterbot.name
        # })

        data = {
            'detail': 'You should make a POST request to this endpoint'
        }

        return JsonResponse(data, status=405)

    def post(self, request, *args, **kwargs):
        """Return a response to the statement in the posted data* The JSON data should contain a text attribute"""
        
        # input_data = json.loads(request.body.decode('utf-8'))
        input_statement = request.POST.get('text')

        # if 'text' not in input_data:
        #     return JsonResponse({
        #         'text': [
        #             'The attribute "text" is required'
        #         ]
        #     }, status=400)

        # response = self.chatterbot.get_response(input_data)
        response_data = {
            'text': chatterbot.get_response(input_statement)
        }

        # response_data = response.serialize()

        return JsonResponse(response_data, status=200)


