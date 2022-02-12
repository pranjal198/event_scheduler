from math import exp
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.http import JsonResponse
from .models import Profile
from .serializer import  ProfileSerializer
from .tasks_helper import * 
from tasks.serializer import TaskSerializer
import jwt,json,time
from event_scheduler import settings
from rest_framework.exceptions import AuthenticationFailed
from django.views.decorators.csrf import csrf_exempt

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
        user,profile = get_user_from_request(request)
        serialised = ProfileSerializer(profile)
        response = JsonResponse(serialised.data,safe=False)
        set_cookie(response,'jwt',generate_token(profile),7)
        return response
    except:
        return JsonResponse({"message":"no such user"},safe=False)

def get_all_rsvp_tasks(request):
    try:
        user,profile = get_user_from_request(request)
        qs = profile.get_rsvp_tasks()
        serialised = TaskSerializer(qs,many=True)
        response = JsonResponse(serialised.data,safe=False)
        set_cookie(response,'jwt',generate_token(profile),7)
        return response
    except:
        return JsonResponse({"message":"no rsvp tasks"},safe=False)

def get_all_other_tasks(request):
    try:
        user,profile = get_user_from_request(request)
        qs = helper_get_not_rsvp_tasks(profile)
        serialised = TaskSerializer(qs,many=True)
        response = JsonResponse(serialised.data,safe=False)
        set_cookie(response,'jwt',generate_token(profile),7)
        return response
    except:
        return JsonResponse({"message":"no new rsvp tasks"},safe=False)

# <str:club_name>
def get_rsvp_club_tasks(request,club_name):
    try:
        user,profile = get_user_from_request(request)
        qs = helper_get_subscribed_club_tasks(profile,club_name)
        serialised = TaskSerializer(qs,many=True)
        response = JsonResponse(serialised.data,safe=False)
        set_cookie(response,'jwt',generate_token(profile),7)
        return response
    except:
        return JsonResponse({"message":"no rsvp tasks for club"},safe=False)

def get_new_club_tasks(request,club_name):
    try:
        user,profile = get_user_from_request(request)
        qs = helper_get_new_club_tasks(profile,club_name)
        serialised = TaskSerializer(qs,many=True)
        response = JsonResponse(serialised.data,safe=False)
        set_cookie(response,'jwt',generate_token(profile),7)
        return response
    except:
        return JsonResponse({"message":"no new rsvp tasks for the club"},safe=False)

def generate_token(profile):
    payload = {
        'user_id': profile.user.id,
        'profile_id': profile.id,
        'club_name': profile.club_name,
        'club_status': profile.club_status,
        'name': profile.name,
        'roll': profile.roll,
        'email': profile.user.email,
        'batch': profile.batch,
        'programme': profile.programme,
        'department': profile.department,
        'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=60),
        'iat':datetime.datetime.utcnow()
    }
    encoded_jwt = jwt.encode(payload,settings.SECRET_KEY , algorithm="HS256")
    return encoded_jwt

@csrf_exempt
def login_via_password(request):
    try:
        data=json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                profile = Profile.objects.filter(user=user).first()
                encoded_jwt = generate_token(profile)
                response = JsonResponse({"message":"success","status":200,"jwt":encoded_jwt})
                set_cookie(response,'jwt',encoded_jwt,7)
                response['jwt'] = encoded_jwt
                return response
            return JsonResponse({"message":"user is unactive","status":400})
        return JsonResponse({"message":"invalid username/password","status":400})
    except:
        print("error")
        return JsonResponse({"message":"error occured","status":400})

@csrf_exempt
def create_generate_jwt(request):
    try:
        data=json.loads(request.body)
        decoded = jwt.decode(data['token'] , options={"verify_signature": False})
        roll = decoded['family_name']
        name = decoded['given_name']
        if(decoded.get('unique_name')):
            email = decoded['unique_name']
        else:
            email = decoded['email']
        exp = decoded['exp']
        if exp > int(time.time()):
            if verify_tenant(email):
                username = get_username(decoded['given_name'])
                user = create_or_get_user(username,email,name,roll)
                profile = Profile.objects.filter(user=user).first()
                encoded_jwt = generate_token(profile)
                response = JsonResponse({"message":"success","status":200,"jwt":encoded_jwt})
                set_cookie(response,'jwt',encoded_jwt,7)
                response['jwt'] = encoded_jwt
                return response
            return JsonResponse({"message":"not authorised for IIT Guwahati","status":400})
        return JsonResponse({"message":"invalid Token","status":400})
    except:
        print("error")
        return JsonResponse({"message":"error occured","status":400})
    
def create_or_get_user(username,email,firstName,lastName):
    user = User.objects.filter(email=email).first()
    if(user):
        return user
    user= User(username=username, email=email,first_name=firstName,last_name=lastName)
    user.save()
    return user

def get_username(name):
    new_name = name.lower()
    modified_str = ''
    for char in range(0, len(new_name)):
        if(new_name[char] == ' '):
            modified_str += '_'
        else:
            modified_str += new_name[char]
    return modified_str

def verify_tenant(email):
    domain = email.split('@')[1]
    return domain=="iitg.ac.in"

import datetime
def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = int(time.time())
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        # domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )
    response['jwt'] = value
    response['Access-Control-Expose-Headers'] = 'jwt'
    
def get_user_from_request(request):
    if(request.user.username):
        profile = Profile.objects.get(user=request.user)
        return request.user,profile
    token = request.COOKIES.get('jwt')
    if not token:
        token = request.headers['Authorization']
        if not token:
            return JsonResponse({"message":"unauthenticated"},status=401)
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse({"message":"unauthenticated"},status=401)
    
    expires = int(time.time())
    if(payload['exp'] < expires ):
        return JsonResponse({"message":"unauthenticated"},status=401)
    
    user = User.objects.filter(id = payload['user_id']).first()
    profile = Profile.objects.filter(id = payload['profile_id']).first()
    return user,profile
