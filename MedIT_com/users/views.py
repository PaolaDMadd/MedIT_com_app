from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def landingpage(request):
    return render(request, 'pages/landingpage.html')

def home(request):
    msg = 'Welcome to MedIT.Com'
    return render(request, 'pages/home.html', {'welcome': msg} )


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
    user = request.user
    args = {'name': user}
    return render(request, 'users/profile.html', args )


