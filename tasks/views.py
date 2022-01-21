from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import my_task
from .serializer import TaskSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.generic import ListView
from users.models import Profile
# from django.views.generic import
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import my_task
from .serializer import TaskSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.generic import ListView
from django.utils.decorators import method_decorator
# from django.views.generic import
# Create your views here.
from tasks.models import my_task
from users.decorators import club
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# from django.contrib.auth import users
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tasks.serializer import TaskSerializer

def index(request):
    param = {
        'tasks': my_task.objects.all()
    }
    return render(request, 'tasks/index.html', param)



class TaskListView(LoginRequiredMixin, ListView):
    model = my_task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = ['date']


@login_required
@api_view(['GET'])
def Get_Task(request):
    """
    List all Tasks, or create a new Task
    """
    Task = my_task.objects.all()
    serializer = TaskSerializer(Task, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET'])
def get_task_detail(request, pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(Task)
    return Response(serializer.data)

@login_required
@club
@api_view(['POST'])
def post_task_detail(request):
    serializer = TaskSerializer(data=request.data)
    if request.data['club_name']!=request.user.profile.club_name:
        return Response({'status':403 , 'message':'club name not matched'})

    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@login_required
@club
@api_view(['PATCH'])
def patch_task_detail(request,pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(Task,data=request.data,partial=True)
  
    if request.data['club_name']!=request.user.profile.club_name:
        return Response({'status':403 , 'message':'club name not matched'})

    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@login_required
@club
@api_view(['PUT'])
def put_task_detail(request,pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(Task,data=request.data,partial=True)

    if request.data['club_name']!=request.user.profile.club_name:
        return Response({'status':403 , 'message':'club name not matched'})

    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@login_required
@club
@api_view(['DELETE'])
def delete_task_detail(request,pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    Task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def rsvp_a_event(request,pk):
    print(pk)
    event = my_task.objects.get(pk=pk)
    event.rsvp_users.add(Profile.objects.get(user=request.user))
    event.save()
    return JsonResponse({'message':'event rsvped'})


def unsub_a_event(request, pk):
    print(pk)
    event = my_task.objects.get(pk=pk)
    event.rsvp_users.remove(Profile.objects.get(user=request.user))
    event.save()
    return JsonResponse({'message':'event unsubscribed'})
