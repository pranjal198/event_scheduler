from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.http import JsonResponse
from .models import Profile
from .serializer import  ProfileSerializer
from .tasks_helper import * 
from tasks.serializer import TaskSerializer

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! please login and update your profile')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Profile has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html',{'title':'profile' , 'u_form':u_form , 'p_form':p_form})

def get_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        serialised = ProfileSerializer(profile)
        return JsonResponse(serialised.data,safe=False)
    except:
        return JsonResponse({"message":"no such user"},safe=False)


def get_all_rsvp_tasks(request):
    try:
        profile = Profile.objects.get(user=request.user)
        qs = profile.get_rsvp_tasks()
        serialised = TaskSerializer(qs,many=True)
        return JsonResponse(serialised.data,safe=False)
    except:
        return JsonResponse({"message":"no rsvp tasks"},safe=False)

def get_all_other_tasks(request):
    try:
        profile = Profile.objects.get(user=request.user)
        qs = helper_get_not_rsvp_tasks(profile)
        serialised = TaskSerializer(qs,many=True)
        return JsonResponse(serialised.data,safe=False)
    except:
        return JsonResponse({"message":"no new rsvp tasks"},safe=False)

# <str:club_name>

def get_rsvp_club_tasks(request,club_name):
    try:
        profile = Profile.objects.get(user=request.user)
        qs = helper_get_subscribed_club_tasks(profile,club_name)
        serialised = TaskSerializer(qs,many=True)
        return JsonResponse(serialised.data,safe=False)
    except:
        return JsonResponse({"message":"no rsvp tasks for club"},safe=False)

def get_new_club_tasks(request,club_name):
    try:
        profile = Profile.objects.get(user=request.user)
        qs = helper_get_new_club_tasks(profile,club_name)
        serialised = TaskSerializer(qs,many=True)
        return JsonResponse(serialised.data,safe=False)
    except:
        return JsonResponse({"message":"no new rsvp tasks for the club"},safe=False)

