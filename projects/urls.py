from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.homepage, name='homepage'),
    path('', views.projects, name='projects'),
    path('view-project/<str:pk>', views.project, name='project'),
    path('add-project', views.add_project, name='add-project'),
    path('update-project/<str:pk>', views.update_project, name='update-project'),
    path('delete-project/<str:pk>', views.delete_project, name='delete-project')
]