from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from .templates import * 
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

# @csrf_exempt
def index(request):
    msg = 'Welcome to MedIT.Com'
    return render(request, 'core_app/index.html', {'welcome': msg} )

# @csrf_protect
def profile(request):
    test = django.middleware.csrf.get_token()
    return render(request, 'core_app/profile.html', {"test": test} )
    

@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect()
    else:
        form = AuthenticationForm()
    return render(request, 'core_app/login.html', {'form': form})


# @csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Welcome, {first_name}!')
            return redirect('core_app/login')
    else:
        form = UserRegisterForm()
    data = {'form': form}
    return render(request, 'core_app/register.html', data)