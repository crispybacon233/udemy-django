from django.shortcuts import render, HttpResponse, redirect
from .forms import ProjectForm
from .models import Project



# Create your views here.

def homepage(request):
    return render(request, 'projects/homepage.html')


def projects(request):
    projObjs = Project.objects.all()
    return render(request, 'projects/projects.html', {'projObjs': projObjs})


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/project.html', {'projectObj': projectObj})


def add_project(request):
    form = ProjectForm

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)