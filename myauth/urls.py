from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('accounts/profile/', views.login,name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='myauth/home.html'), name='logout'),
]