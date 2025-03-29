from django.shortcuts import render

# Create your views here.
def profiles_page(request):
    return render(request, 'users/profiles.html')