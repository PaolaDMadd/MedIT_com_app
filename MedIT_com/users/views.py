from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from diagnosis.templates import *


def landingpage(request):
    return render(request, 'pages/landingpage.html')

def register(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                                    )
            login(req, new_user)
            username = form.cleaned_data.get('username')
            messages.success(req, f'Welcome, {username}!')
            return redirect('profile')
    else:
        form = UserSignupForm()
    data = {'form': form}
    return render(req, 'users/register.html', data)

@login_required
def profile(request):
    return render(request, 'profile.html')
