from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path('projects', views.projects, name='projects'),
    path('projects/<int:slug>', views.project, name='project')
]