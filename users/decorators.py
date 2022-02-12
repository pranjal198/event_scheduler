from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import jwt,time
from event_scheduler import settings
from django.contrib.auth.models import User
from users.models import Profile
from django.http import JsonResponse
from users.views import get_user_from_request
# Custom Decorator
def club(function):
    def _function(request, *args, **kwargs):
        user,profile = get_user_from_request(request)
        if user.is_superuser:
            return function(request, *args, **kwargs)
        if not profile.club_status:
            if not request.user.username:
                return JsonResponse({"message":"unauthenticated"},status=401)
            messages.info(request, 'You Are Not A Club Member')
            return HttpResponseRedirect(reverse('tasks-home'))
        return function(request, *args, **kwargs)

    return _function


def swagger(function):
    def _function(request, *args, **kwargs):
        user,profile = get_user_from_request(request)
        if user.is_superuser:
            return function(request, *args, **kwargs)
        if not profile.club_status:
            messages.info(request, 'You Are Not A Club Member')
            return HttpResponseRedirect(reverse('tasks-home'))
        return function(request, *args, **kwargs)

    return _function


def login_is_required(function):
    def _function(request, *args, **kwargs):
        if(request.user.username):
            if request.user.is_authenticated:
                return function(request, *args, **kwargs)
            messages.info(request, 'You Are Not Authenticated')
            return HttpResponseRedirect(reverse('tasks-home'))
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
        try:
            user = User.objects.filter(id = payload['user_id']).first()
            profile = Profile.objects.filter(id = payload['profile_id']).first()
        except:
            return JsonResponse({"message":"unauthenticated"},status=401)
        
        return function(request, *args, **kwargs)

    return _function
