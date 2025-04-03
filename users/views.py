from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile

# Create your views here.

def logout_page(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login-page')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist.')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('profiles-page')
        else:
            messages.error(request, 'Username or password is incorrect')

    return render(request, 'users/login_register.html')


def profiles_page(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})


def user_profile_page(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'users/user-profile.html', {'profile': profile})