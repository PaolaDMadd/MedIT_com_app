from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from .templates import *

from .forms import MessageForm

chatterbot = ChatBot('MediBot')

trainer = ListTrainer(chatterbot)

trainer.train([
    'Test 1',
    'Test 1 response',
    'Test 2',
    'Test 2 response',
    'Test 3',
    'Test 3 response'
])

trainer.train([
    "Hello",
    "Hi, can I help you?",
    "I'm allergic to Bacitracin",
    "You are not allergic to Bacitracin, you do have a mild allergy to Peanuts",
    "Yes, I have a fever and I have been coughing and sneezing",
    """Looks like you may have the Common Flu (Influenza), make sure 
    you get a lot of rest, and drink plenty of fluids, if you are in
    a lot of pain over the counter painkillers such as ibuprofen can help, 
    please contact your doctor if your symptoms worsen, or persist for over two weeks.
    Can I help you with anything else?""",
    "Yes, I have a cough and lots of mucus",
    """Looks like you may have a Chest Cold (Acute Bronchitis), make sure
    you get a lot of rest and drink plenty of fluids, you can take lozenges
    (if older than 4) or use honey to sooth your throat, please contact your
    doctor if your symptoms worsen, or persist for over two weeks.
    Can I help you with anything else?""",
    "No, thank you",
    "You're welcome have a nice day!"
])

@csrf_exempt
def get_response(request):

    response = {'status': None}

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['message']

            chat_response = chatterbot.get_response(data).text
            response['message'] ={'text': chat_response, 'user': False, 'chat_bot': True}
            response['status'] = 'success'

        return render(request, 'chat.html', {'form': form, 'message': chat_response})

    else:
        form = MessageForm()
        return render(request, 'chat.html', {'form': form})