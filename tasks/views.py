from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import my_task
from .serializer import TaskSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.generic import ListView
# from django.views.generic import
# Create your views here.
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

class myTaskListAPI(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = my_task.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('club_name','title', 'description', 'author__profile__name')


class myTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = my_task.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class myTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = TaskSerializer
    queryset = my_task.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)
class myTaskUpdateAPI(generics.GenericAPIView, mixins.UpdateModelMixin):
    serializer_class = TaskSerializer
    queryset = my_task.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def put(self, request, pk):
        return self.update(request, pk)
