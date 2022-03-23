from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
import jwt
from users.views import generate_token, get_user_from_request, set_cookie
from .models import my_task
from .serializer import TaskSerializer
from django.views.generic import ListView
from users.decorators import club,login_is_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.core.files.storage import default_storage
from users.signals import schedule_add,schedule_update,schedule_delete
from event_scheduler import settings

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
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
@login_is_required
@club
@api_view(['POST'])
def post_task_detail(request):
    user,profile = get_user_from_request(request)
    if request.data['club_name']!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'Club Name Not Matched '})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    print(request.data)
    data = request.data
    data['location'] = {
        'offline':{
            'latitude':'',
            'longitude':''
        },
        'online':{
            'meet_url':'',
            'room_id':'',
            'password':''
        }
    }
    data['announcement'] = {
        'fixed':[],
        'dynamic':[],
    }
    data['payment'] = {
        'paid':False,
        'metadata':{
            'price':0,
            'link':''
        }
    }
    data['emails'] = {
        'registration':{
            'to':[],
            'sub':'',
            'body':''
        },
        'scheduled':[]
    }
    data['feedback'] = {
        '1':[],
        '2':[],
        '3':[],
        '4':[],
        '5':[]
    }
    data['all_ids'] = {
        'guests':0,
        'fixed':0,
        'dynamic':0,
        'drive_links':0,
        'scheduled':0,
        'resources_upload':0,
        }
    serializer = TaskSerializer(data=request.data)
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
@api_view(['PUT'])
def put_json_fields(request,pk):
    user,profile = get_user_from_request(request)
    try:
        event = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        response = Response(status=status.HTTP_404_NOT_FOUND)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    
    if event.club_name!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'event Is Not Created by '+profile.club_name})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    data = request.data
    # try:
    if data['field'] == 'guests':
        if data['method'] == 'ADD':
            event.all_ids['guests'] += 1
            data['data']['id'] = event.all_ids['guests']
            event.guests.append(data['data'])
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})

        if data['method'] == 'UPDATE':
            id = data['id']
            data['data']['id']=id
            for resource in event.guests:
                if resource['id'] == id:
                    found = resource
            event.guests.remove(found)
            event.guests.append(data['data'])
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
        if data['method'] == 'DELETE':
            id = data['id']
            for resource in event.guests:
                if resource['id'] == id:
                    found = resource
            event.guests.remove(found)
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
    if data['field'] == 'location':
        if data['method'] == 'UPDATE':
            event.location[data['mode']] = data['data']
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
        if data['method'] == 'DELETE':
            demo = {
                    'offline':{
                        'latitude':'',
                        'longitude':''
                    },
                    'online':{
                        'meet_url':'',
                        'room_id':'',
                        'password':''
                    }
            }
            event.location[data['mode']] = demo[data['mode']]
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
    if data['field'] == 'announcement':
        if data['method'] == 'ADD':
            event.all_ids[data['mode']] += 1
            data['data']['id']=event.all_ids[data['mode']]
            event.announcement[data['mode']].append(data['data'])
            event.save()
            if data['mode']=='fixed':
                """
                    Send the Notification of follwing announcement to its rsvp_users via websockets
                """
            schedule_add.send(sender=my_task,instance=event,field="announcement",id=event.all_ids[data['mode']],data=data['data'])
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})

        if data['method'] == 'UPDATE':
            id = data['id']
            data['data']['id']=id
            for announcement in event.announcement[data['mode']]:
                if announcement['id'] == id:
                    found = announcement
            event.announcement[data['mode']].remove(found)
            event.announcement[data['mode']].append(data['data'])
            event.save()
            if data['mode']=='fixed':
                """
                    Send the Notification of follwing announcement update to its rsvp_users via websockets
                """
            schedule_update.send(sender=my_task,instance=event,field="announcement",id=id,data=data['data'])
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
        if data['method'] == 'DELETE':
            id = data['id']
            schedule_delete.send(sender=my_task,instance=event,field="announcement",id=id)
            for announcement in event.announcement[data['mode']]:
                if announcement['id'] == id:
                    found = announcement
            event.announcement[data['mode']].remove(found)
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
    if data['field'] == 'drive_links':
        if data['method'] == 'ADD':
            event.all_ids['drive_links'] += 1
            data['data']['id']=event.all_ids['drive_links']
            event.drive_links.append(data['data'])
            event.save()
            """
                Send the Notification of follwing drive_links uploaded to its rsvp_users via websockets
            """
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})

        if data['method'] == 'UPDATE':
            id = data['id']
            data['data']['id']=id
            for drive_link in event.drive_links:
                if drive_link['id'] == id:
                    found = drive_link
            event.drive_links.remove(found)
            event.drive_links.append(data['data'])
            event.save()
            """
                Send the Notification of follwing drive_links updated to its rsvp_users via websockets
            """
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
        if data['method'] == 'DELETE':
            id = data['id']
            data['data']['id']=id
            for drive_link in event.drive_links:
                if drive_link['id'] == id:
                    found = drive_link
            event.drive_links.remove(found)
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
    if data['field'] == 'payment':
        if data['method'] == 'ADD':
            event.payment['paid']=True
            event.payment['metadata']=data['data']
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})

        if data['method'] == 'UPDATE':
            event.payment['metadata']=data['data']
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
        if data['method'] == 'DELETE':
            event.payment['paid']=False
            event.payment['metadata']={
                                    'price':0,
                                    'link':''
                                }
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
    if data['field'] == 'emails':
        if data['method'] == 'ADD':
            if data['mode']=='scheduled':
                event.all_ids['scheduled'] += 1
                data['data']['id']=event.all_ids['scheduled']
                event.emails[data['mode']].append(data['data'])
                schedule_add.send(sender=my_task,instance=event,field="emails",id=event.all_ids['scheduled'],data=data['data'])
            else:
                event.emails[data['mode']]=data['data']
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})

        if data['method'] == 'UPDATE':
            if data['mode']=='scheduled':
                id = data['id']
                data['data']['id']=id
                for email in event.emails[data['mode']]:
                    if email['id'] == id:
                        found = email
                event.emails[data['mode']].remove(found)
                event.emails[data['mode']].append(data['data'])
                schedule_update.send(sender=my_task,instance=event,field="emails",id=id,data=data['data'])
            else:
                event.emails[data['mode']]=data['data']
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
        if data['method'] == 'DELETE':
            if data['mode']=='scheduled':
                id = data['id']
                for email in event.emails[data['mode']]:
                    if email['id'] == id:
                        found = email
                schedule_delete.send(sender=my_task,instance=event,field="emails",id=id)
                event.emails[data['mode']].remove(found)
            else:
                event.emails[data['mode']]={
                                            'to':[],
                                            'sub':'',
                                            'body':''
                                        }
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
    if data['field'] == 'resources_upload':
        if data['method'] == 'ADD':
            event.all_ids['resources_upload'] += 1
            new_data = {}
            new_data['id'] = event.all_ids['resources_upload']
            new_data['filename'] = data['data']
            uploaded_file = request.FILES['file']
            filename = uploaded_file.name
            ext = filename.split('.')[1]
            new_name = data['data']+'.'+ext
            default_storage.save('events/event-'+str(event.id)+'/resources/'+new_name,uploaded_file)
            file_url = default_storage.url('events/event-'+str(event.id)+'/resources/'+new_name)
            new_data['url']=file_url
            event.resources_upload.append(new_data)
            event.save()
            """
                Send the Notification of follwing resouce uploaded to its rsvp_users via websockets
            """
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
            
        if data['method'] == 'DELETE':
            id = data['id']
            for resource in event.resources_upload:
                if resource['id'] == id:
                    found = resource
            url = found['url']
            arr = url.split('/')
            l = False
            path = 'events'
            for item in arr:
                if l:
                    path += '/'+item
                if item == 'events':
                    l = True
            default_storage.delete(path)
            event.resources_upload.remove(found)
            event.save()
            serializer = TaskSerializer(event)
            response = JsonResponse({'message':serializer.data})
        
    # except:
    #     response = JsonResponse({'message':"please provide vaild parameters","status":404})
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response

@login_is_required
@club
@api_view(['DELETE'])
def delete_task_detail(request,pk):
    user,profile = get_user_from_request(request)
    try:
        event = my_task.objects.get(pk=pk)
    except my_task.DoesNotExist:
        response = Response(status=status.HTTP_404_NOT_FOUND)
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    


    if event.club_name!=profile.club_name and not user.is_superuser:
        response = Response({'status':403 , 'message':'event Is Not Created by '+profile.club_name+" so you can't delete this task."})
        token = generate_token(profile)
        set_cookie(response,'jwt',token)
        return response
    
    event.delete()
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

@login_is_required
def page_view(request,pk):
    event = my_task.objects.get(pk=pk)
    user,profile = get_user_from_request(request)
    x = timezone.localtime(timezone.now()).date()
    date = x.strftime('%Y-%m-%d')
    if date in event.page_view.keys():
        if not profile.id in event.page_view[date]:
            event.page_view[date].append(profile.id)
    else:
        event.page_view[date] = []
        event.page_view[date].append(profile.id)
    event.save()
    response = JsonResponse({'message':"ok"})
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response
    
@login_is_required
@api_view(['POST'])
def feedback(request,pk):
    event = my_task.objects.get(pk=pk)
    user,profile = get_user_from_request(request)
    data = request.data
    for key in event.feedback:
        if profile.id in event.feedback[key]:
            event.feedback[key].remove(profile.id)
    event.feedback[data['rating']].append(profile.id)
    event.save()
    response = JsonResponse({'message':"feedback added"})
    token = generate_token(profile)
    set_cookie(response,'jwt',token)
    return response

@login_is_required
@club
@api_view(['POST'])
def invite_guest(request):
    data = request.data
    payload = {}
    payload['name'] = data['name']
    payload['email'] = data['email']
    payload['event_id'] = data['event_id']
    payload['accepted'] = False
    message = data['message']
    try:
        event = my_task.objects.get(id=payload['event_id'])
        event.all_ids['guests'] += 1
        payload['id'] = event.all_ids['guests']
        event.guests.append(payload)
        event.save()
        encoded_jwt = jwt.encode(payload,settings.SECRET_KEY , algorithm="HS256")
        url = "localhost:3000/"+payload['event_id']+"/"+encoded_jwt
        """
            send email to guest containing message and url
        """
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def accept_invite(request):
    data = request.data
    encoded_jwt = data['jwt']
    try:
        payload = jwt.decode(encoded_jwt, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return JsonResponse({"message":"unauthorised guest"},status=401)
    id = payload['id']
    payload['accepted'] = True
    try:
        event = my_task.objects.get(id=payload['event_id'])
        for resource in event.guests:
            if resource['id'] == id:
                found = resource
        event.guests.remove(found)
        event.guests.append(payload)
        event.save()
        return Response("accepted",status=status.HTTP_200_OK)
    except:
        return Response("event doesn't exists",status=status.HTTP_400_BAD_REQUEST)