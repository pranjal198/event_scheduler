from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile(request):
    return render(request, 'users/profile.html',{'title':'profile'})