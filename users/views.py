from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles_page(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})


def user_profile_page(request, pk):
    profile = Profile.objects.get(id=pk)
    return render(request, 'users/user-profile.html', {'profile': profile})