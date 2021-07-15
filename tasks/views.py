from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Task
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters.rest_framework




class TaskListAPI(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)
    queryset = Task.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title','description','author__name')


class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)



class TaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_class=(permissions.IsAuthenticatedOrReadOnly,)


    def post(self, request):
        return self.create(request)

# Create your views here.
def index(request):
    param={
        'tasks': Task.objects.all()
    }
    return render(request, 'tasks/index.html',param)

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name='tasks/index.html'
    context_object_name='tasks'
    ordering = ['date']


class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task




class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','event_type','target_batch','target_branch','date','time_from','time_to','description']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class TaskUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','event_type','target_batch','target_branch','date','time_from','time_to','description']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

class TaskDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False
