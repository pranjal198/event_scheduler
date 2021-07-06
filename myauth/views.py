from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.contrib.auth import logout as auth_logout
# Create your views here.
def home(request):
    return render(request, 'myauth/index.html')

def login(request):
    return render(request, 'myauth/index.html')

def remove_user_and_token(request):
  if 'token_cache' in request.session:
    del request.session['token_cache']

  if 'user' in request.session:
    del request.session['user']

def preloader(request):
    return render(request, 'myauth/index.html')
def sign_out(request):
    remove_user_and_token(request)
    return HttpResponseRedirect(reverse('index'))


