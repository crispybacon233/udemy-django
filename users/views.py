from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            user = User.objects.get(username=username)
        except:
            print('Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('profiles-page')
        else:
            print('Username OR password is incorrect')

    return render(request, 'users/login_register.html')


def profiles_page(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})


def user_profile_page(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'users/user-profile.html', {'profile': profile})