from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from .models import User
from django.contrib.auth import authenticate, login
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
    


def login(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            user_id = user.id
            return redirect(f'core_app/profile{user_id}')
        else:
            print('user not authenticate')
            form = UserLoginForm()
            return render(request, 'core_app/login.html', {'form': form})

    else:
        form = UserLoginForm()
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