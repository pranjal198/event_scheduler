from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('accounts/profile/', views.login,name="login")
]