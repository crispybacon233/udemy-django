from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.logout_page, name='logout-page'),
    path('login/', views.login_page, name='login-page'),
    path('', views.profiles_page, name='profiles-page'),
    path('profile/<str:pk>', views.user_profile_page, name='user-profile-page')
]