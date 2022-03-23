from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from users.views import generate_token, get_user_from_request, set_cookie
from .models import Club
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
		'clubs': Club.objects.all()
	}
	return render(request, 'clubs/index.html', param)



class ClubListView(LoginRequiredMixin, ListView):
	model = Club
	template_name = 'clubs/index.html'
	context_object_name = 'clubs'
	ordering = ['date']


@login_is_required
@api_view(['GET'])
def Get_Club(request):
	"""
	List all Clubs, or create a new Club
	"""
	club = Club.objects.all()
	serializer = ClubSerializer(club, many=True)
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
		club = Club.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = ClubSerializer(club)
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
	if Club.objects.filter(club_name=profile.club_name).exists():
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
		club = Club.objects.get(pk=pk)
	except club.DoesNotExist:
		response = Response(status=status.HTTP_404_NOT_FOUND)
		token = generate_token(profile)
		set_cookie(response,'jwt',token)
		return response

	serializer = ClubSerializer(Club,data=request.data,partial=True)
	

	if club.club_name!=profile.club_name and not user.is_superuser:
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
		club = Club.objects.get(pk=pk)
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
		event = Club.objects.get(pk=pk)
	except Club.DoesNotExist:
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



