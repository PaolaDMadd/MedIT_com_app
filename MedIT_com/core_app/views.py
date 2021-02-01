from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(req):
    return HttpResponse("<h1>Hello! welcome index page!<h1>")

def show(req):
    return HttpResponse('<h3>welcome show page!</h3>')

def login(req):
    if request.method == 'POST':
        form = AutenticationForm(data = request.POST)
        if form.is_valid():

    return HttpResponse("hello from login")

def register(req):
    return HttpResponse("hello from register")