from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from users.views import get_user_from_request
from .models import my_task
from .serializer import TaskSerializer
from django.views.generic import ListView
from users.decorators import club,login_is_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


@login_is_required
@api_view(['GET'])
def Get_Task(request):
    """
    List all Tasks, or create a new Task
    """
    Task = my_task.objects.all()
    serializer = TaskSerializer(Task, many=True)
    return Response(serializer.data)


@login_is_required
@api_view(['GET'])
def get_task_detail(request, pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(Task)
    return Response(serializer.data)

@login_is_required
@club
@api_view(['POST'])
def post_task_detail(request):
    serializer = TaskSerializer(data=request.data)
    user,profile = get_user_from_request(request)
    if request.data['club_name']!=profile.club_name:
        return Response({'status':403 , 'message':'Club Name Not Matched '})


    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@login_is_required
@club
@api_view(['PATCH'])
def patch_task_detail(request,pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(Task,data=request.data,partial=True)
    
    user,profile = get_user_from_request(request)

    if Task.club_name!=profile.club_name:
        return Response({'status':403 , 'message':'Task Is Not Created by '+profile.club_name})
    
    # if request.data['club_name']!=profile.club_name:
    #     return Response({'status':403 , 'message':'club name not matched'})

    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@login_is_required
@club
@api_view(['PUT'])
def put_task_detail(request,pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(Task,data=request.data,partial=True)
    
    user,profile = get_user_from_request(request)

    if Task.club_name!=profile.club_name:
        return Response({'status':403 , 'message':'Task Is Not Created by '+profile.club_name})

    if Task.data['club_name']!=profile.club_name:
        return Response({'status':403 , 'message':'club name not matched'})

    if not serializer.is_valid():
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@login_is_required
@club
@api_view(['DELETE'])
def delete_task_detail(request,pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user,profile = get_user_from_request(request)


    if Task.club_name!=profile.club_name:
        return Response({'status':403 , 'message':'Task Is Not Created by '+profile.club_name+" so you can't delete this task."})
    
    Task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@login_is_required
def rsvp_a_event(request,pk):
    event = my_task.objects.get(pk=pk)
    user,profile = get_user_from_request(request)
    event.rsvp_users.add(profile)
    event.save()
    return JsonResponse({'message':"event RSVP'ed"})

@login_is_required
def unsub_a_event(request, pk):
    event = my_task.objects.get(pk=pk)
    user,profile = get_user_from_request(request)
    event.rsvp_users.remove(profile)
    event.save()
    return JsonResponse({'message':'event Unsubscribed'})
