from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles_page(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})