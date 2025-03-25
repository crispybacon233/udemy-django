from django.shortcuts import render, HttpResponse
from .models import Project



# Create your views here.
def homepage(request):
    return render(request, 'projects/homepage.html')


def projects(request):
    projObjs = Project.objects.all()
    return render(request, 'projects/projects.html', {'projObjs': projObjs})


def project(request, slug):
    projectObj = Project.objects.get(id=slug)
    return render(request, 'projects/project.html', {'projectObj': projectObj})