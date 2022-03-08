from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from users.views import generate_token, get_user_from_request, set_cookie
from .models import club
from .serializer import ClubSerializer
from django.views.generic import ListView
from users.decorators import club as clubs,login_is_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.core.files.storage import default_storage
from users.signals import schedule_add,schedule_update,schedule_delete
from rest_framework import serializers
from rest_framework import status

def index(request):
	param = {
		'clubs': club.objects.all()
	}
	return render(request, 'clubs/index.html', param)



class ClubListView(LoginRequiredMixin, ListView):
	model = club
	template_name = 'clubs/index.html'
	context_object_name = 'clubs'
	ordering = ['date']


@login_is_required
@api_view(['GET'])
def Get_Club(request):
	"""
	List all Clubs, or create a new Club
	"""
	Club = club.objects.all()
	serializer = ClubSerializer(Club, many=True)
	response =  Response(serializer.data)
	user,profile = get_user_from_request(request)
	token = generate_token(profile)
	set_cookie(response,'jwt',token)
	return response


@login_is_required
@api_view(['GET'])
def get_club_detail(request, pk):
	"""
	List Club according to the request parameter in the url
	"""
	try:
		Club = club.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = ClubSerializer(Club)
	response =  Response(serializer.data)
	user,profile = get_user_from_request(request)
	token = generate_token(profile)
	set_cookie(response,'jwt',token)
	return response
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
@login_is_required
@clubs
@api_view(['POST'])
def post_club_detail(request):
	"""
	Create A New Club 
	"""


	user,profile = get_user_from_request(request)


	if request.data['club_name']!=profile.club_name and not user.is_superuser:
		response = Response({'status':403 , 'message':'Club Name Not Matched '})
		token = generate_token(profile)
		set_cookie(response,'jwt',token)
		return response
	print(request.data)
	data = request.data    
	serializer = ClubSerializer(data=request.data)
	if club.objects.filter(club_name=profile.club_name).exists():
		raise serializers.ValidationError('This Club already exists')

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
@clubs
@api_view(['PATCH'])
def patch_club_detail(request,pk):
	"""
	Edit Specific parameters of A Club according to the request parameter in the url
	"""
	user,profile = get_user_from_request(request)
	try:
		Club = club.objects.get(pk=pk)
	except club.DoesNotExist:
		response = Response(status=status.HTTP_404_NOT_FOUND)
		token = generate_token(profile)
		set_cookie(response,'jwt',token)
		return response

	serializer = ClubSerializer(Club,data=request.data,partial=True)
	

	if Club.club_name!=profile.club_name and not user.is_superuser:
		response = Response({'status':403 , 'message':'Club Profile Is Not Created by '+profile.club_name+', so you cannot edit this club details'})
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
@clubs
@api_view(['PUT'])
def put_club_detail(request,pk):
	"""
	Edit All details of A Club according to the request parameter int the url
	"""
	user,profile = get_user_from_request(request)
	try:
		Club = club.objects.get(pk=pk)
	except club.DoesNotExist:
		response = Response(status=status.HTTP_404_NOT_FOUND)
		token = generate_token(profile)
		set_cookie(response,'jwt',token)
		return response

	serializer = ClubSerializer(Club,data=request.data,partial=True)
	

	if Task.club_name!=profile.club_name and not user.is_superuser:
		response = Response({'status':403 , 'message':'Club Profile Is Not Created by '+profile.club_name})
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
@clubs
@api_view(['DELETE'])
def delete_club_detail(request,pk):
	user,profile = get_user_from_request(request)
	try:
		event = club.objects.get(pk=pk)
	except club.DoesNotExist:
		response = Response(status=status.HTTP_404_NOT_FOUND)
		token = generate_token(profile)
		set_cookie(response,'jwt',token)
		return response
	


	if event.club_name!=profile.club_name and not user.is_superuser:
		response = Response({'status':403 , 'message':'Club Profile Is Not Created by '+profile.club_name+" so you can't delete this Club Profile."})
		token = generate_token(profile)
		set_cookie(response,'jwt',token)
		return response
	
	event.delete()
	response = Response(status=status.HTTP_204_NO_CONTENT)
	token = generate_token(profile)
	set_cookie(response,'jwt',token)
	return response



# @login_is_required
# @club
# @api_view(['PUT'])
# def put_json_fields(request,pk):
#     user,profile = get_user_from_request(request)
#     try:
#         event = club.objects.get(pk=pk)
#     except club.DoesNotExist:
#         response = Response(status=status.HTTP_404_NOT_FOUND)
#         token = generate_token(profile)
#         set_cookie(response,'jwt',token)
#         return response
	
#     if event.club_name!=profile.club_name and not user.is_superuser:
#         response = Response({'status':403 , 'message':'event Is Not Created by '+profile.club_name})
#         token = generate_token(profile)
#         set_cookie(response,'jwt',token)
#         return response
#     data = request.data
#     # try:
#     if data['field'] == 'guests':
#         if data['method'] == 'ADD':
#             event.all_ids['guests'] += 1
#             data['data']['id'] = event.all_ids['guests']
#             event.guests.append(data['data'])
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})

#         if data['method'] == 'UPDATE':
#             id = data['id']
#             data['data']['id']=id
#             for resource in event.guests:
#                 if resource['id'] == id:
#                     found = resource
#             event.guests.remove(found)
#             event.guests.append(data['data'])
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#         if data['method'] == 'DELETE':
#             id = data['id']
#             for resource in event.guests:
#                 if resource['id'] == id:
#                     found = resource
#             event.guests.remove(found)
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#     if data['field'] == 'location':
#         if data['method'] == 'UPDATE':
#             event.location[data['mode']] = data['data']
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#         if data['method'] == 'DELETE':
#             demo = {
#                     'offline':{
#                         'latitude':'',
#                         'longitude':''
#                     },
#                     'online':{
#                         'meet_url':'',
#                         'room_id':'',
#                         'password':''
#                     }
#             }
#             event.location[data['mode']] = demo[data['mode']]
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#     if data['field'] == 'announcement':
#         if data['method'] == 'ADD':
#             event.all_ids[data['mode']] += 1
#             data['data']['id']=event.all_ids[data['mode']]
#             event.announcement[data['mode']].append(data['data'])
#             event.save()
#             if data['mode']=='fixed':
#                 """
#                     Send the Notification of follwing announcement to its rsvp_users via websockets
#                 """
#             schedule_add.send(sender=club,instance=event,field="announcement",id=event.all_ids[data['mode']],data=data['data'])
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})

#         if data['method'] == 'UPDATE':
#             id = data['id']
#             data['data']['id']=id
#             for announcement in event.announcement[data['mode']]:
#                 if announcement['id'] == id:
#                     found = announcement
#             event.announcement[data['mode']].remove(found)
#             event.announcement[data['mode']].append(data['data'])
#             event.save()
#             if data['mode']=='fixed':
#                 """
#                     Send the Notification of follwing announcement update to its rsvp_users via websockets
#                 """
#             schedule_update.send(sender=club,instance=event,field="announcement",id=id,data=data['data'])
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#         if data['method'] == 'DELETE':
#             id = data['id']
#             schedule_delete.send(sender=club,instance=event,field="announcement",id=id)
#             for announcement in event.announcement[data['mode']]:
#                 if announcement['id'] == id:
#                     found = announcement
#             event.announcement[data['mode']].remove(found)
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#     if data['field'] == 'drive_links':
#         if data['method'] == 'ADD':
#             event.all_ids['drive_links'] += 1
#             data['data']['id']=event.all_ids['drive_links']
#             event.drive_links.append(data['data'])
#             event.save()
#             """
#                 Send the Notification of follwing drive_links uploaded to its rsvp_users via websockets
#             """
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})

#         if data['method'] == 'UPDATE':
#             id = data['id']
#             data['data']['id']=id
#             for drive_link in event.drive_links:
#                 if drive_link['id'] == id:
#                     found = drive_link
#             event.drive_links.remove(found)
#             event.drive_links.append(data['data'])
#             event.save()
#             """
#                 Send the Notification of follwing drive_links updated to its rsvp_users via websockets
#             """
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#         if data['method'] == 'DELETE':
#             id = data['id']
#             data['data']['id']=id
#             for drive_link in event.drive_links:
#                 if drive_link['id'] == id:
#                     found = drive_link
#             event.drive_links.remove(found)
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#     if data['field'] == 'payment':
#         if data['method'] == 'ADD':
#             event.payment['paid']=True
#             event.payment['metadata']=data['data']
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})

#         if data['method'] == 'UPDATE':
#             event.payment['metadata']=data['data']
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#         if data['method'] == 'DELETE':
#             event.payment['paid']=False
#             event.payment['metadata']={
#                                     'price':0,
#                                     'link':''
#                                 }
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#     if data['field'] == 'emails':
#         if data['method'] == 'ADD':
#             if data['mode']=='scheduled':
#                 event.all_ids['scheduled'] += 1
#                 data['data']['id']=event.all_ids['scheduled']
#                 event.emails[data['mode']].append(data['data'])
#                 schedule_add.send(sender=club,instance=event,field="emails",id=event.all_ids['scheduled'],data=data['data'])
#             else:
#                 event.emails[data['mode']]=data['data']
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})

#         if data['method'] == 'UPDATE':
#             if data['mode']=='scheduled':
#                 id = data['id']
#                 data['data']['id']=id
#                 for email in event.emails[data['mode']]:
#                     if email['id'] == id:
#                         found = email
#                 event.emails[data['mode']].remove(found)
#                 event.emails[data['mode']].append(data['data'])
#                 schedule_update.send(sender=club,instance=event,field="emails",id=id,data=data['data'])
#             else:
#                 event.emails[data['mode']]=data['data']
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#         if data['method'] == 'DELETE':
#             if data['mode']=='scheduled':
#                 id = data['id']
#                 for email in event.emails[data['mode']]:
#                     if email['id'] == id:
#                         found = email
#                 schedule_delete.send(sender=club,instance=event,field="emails",id=id)
#                 event.emails[data['mode']].remove(found)
#             else:
#                 event.emails[data['mode']]={
#                                             'to':[],
#                                             'sub':'',
#                                             'body':''
#                                         }
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#     if data['field'] == 'resources_upload':
#         if data['method'] == 'ADD':
#             event.all_ids['resources_upload'] += 1
#             new_data = {}
#             new_data['id'] = event.all_ids['resources_upload']
#             new_data['filename'] = data['data']
#             uploaded_file = request.FILES['file']
#             filename = uploaded_file.name
#             ext = filename.split('.')[1]
#             new_name = data['data']+'.'+ext
#             default_storage.save('events/event-'+str(event.id)+'/resources/'+new_name,uploaded_file)
#             file_url = default_storage.url('events/event-'+str(event.id)+'/resources/'+new_name)
#             new_data['url']=file_url
#             event.resources_upload.append(new_data)
#             event.save()
#             """
#                 Send the Notification of follwing resouce uploaded to its rsvp_users via websockets
#             """
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
			
#         if data['method'] == 'DELETE':
#             id = data['id']
#             for resource in event.resources_upload:
#                 if resource['id'] == id:
#                     found = resource
#             url = found['url']
#             arr = url.split('/')
#             l = False
#             path = 'events'
#             for item in arr:
#                 if l:
#                     path += '/'+item
#                 if item == 'events':
#                     l = True
#             default_storage.delete(path)
#             event.resources_upload.remove(found)
#             event.save()
#             serializer = ClubSerializer(event)
#             response = JsonResponse({'message':serializer.data})
		
#     # except:
#     #     response = JsonResponse({'message':"please provide vaild parameters","status":404})
#     token = generate_token(profile)
#     set_cookie(response,'jwt',token)
#     return response
