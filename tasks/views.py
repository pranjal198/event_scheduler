from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from users.views import generate_token, get_user_from_request, set_cookie
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
    response =  Response(serializer.data)
    user,profile = get_user_from_request(request)
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response


@login_is_required
@api_view(['GET'])
def get_task_detail(request, pk):
    try:
        Task = my_task.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(Task)
    response =  Response(serializer.data)
    user,profile = get_user_from_request(request)
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response

@login_is_required
@club
@api_view(['POST'])
def post_task_detail(request):
    serializer = TaskSerializer(data=request.data)
    user,profile = get_user_from_request(request)
    if request.data['club_name']!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'Club Name Not Matched '})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response


    if not serializer.is_valid():
        response = Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response

    if serializer.is_valid():
        serializer.save()
        response = Response(serializer.data,status=status.HTTP_201_CREATED)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response


@login_is_required
@club
@api_view(['PATCH'])
def patch_task_detail(request,pk):
    user,profile = get_user_from_request(request)
    try:
        Task = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        response = Response(status=status.HTTP_404_NOT_FOUND)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response

    serializer = TaskSerializer(Task,data=request.data,partial=True)
    

    if Task.club_name!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'Task Is Not Created by '+profile.club_name})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    
    # if request.data['club_name']!=profile.club_name:
    #     return Response({'status':403 , 'message':'club name not matched'})

    if not serializer.is_valid():
        response = Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response

    if serializer.is_valid():
        serializer.save()
        response = Response(serializer.data,status=status.HTTP_201_CREATED)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response


@login_is_required
@club
@api_view(['PUT'])
def put_task_detail(request,pk):
    user,profile = get_user_from_request(request)
    try:
        Task = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        response = Response(status=status.HTTP_404_NOT_FOUND)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response

    serializer = TaskSerializer(Task,data=request.data,partial=True)
    

    if Task.club_name!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'Task Is Not Created by '+profile.club_name})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response

    if Task.data['club_name']!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'club name not matched'})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response

    if not serializer.is_valid():
        response = Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response

    if serializer.is_valid():
        serializer.save()
        response = Response(serializer.data,status=status.HTTP_201_CREATED)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response


@login_is_required
@club
@api_view(['DELETE'])
def delete_task_detail(request,pk):
    user,profile = get_user_from_request(request)
    try:
        Task = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        response = Response(status=status.HTTP_404_NOT_FOUND)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    


    if Task.club_name!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'Task Is Not Created by '+profile.club_name+" so you can't delete this task."})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    
    Task.delete()
    response = Response(status=status.HTTP_204_NO_CONTENT)
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response

@login_is_required
def rsvp_a_event(request,pk):
    event = my_task.objects.get(pk=pk)
    user,profile = get_user_from_request(request)
    event.rsvp_users.add(profile)
    event.save()
    response = JsonResponse({'message':"event RSVP'ed"})
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response

@login_is_required
def unsub_a_event(request, pk):
    event = my_task.objects.get(pk=pk)
    user,profile = get_user_from_request(request)
    event.rsvp_users.remove(profile)
    event.save()
    response = JsonResponse({'message':'event Unsubscribed'})
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response
