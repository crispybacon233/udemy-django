from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('', views.profiles_page, name='profiles-page'),
    path('profile/<str:pk>', views.user_profile_page, name='user-profile-page')
]