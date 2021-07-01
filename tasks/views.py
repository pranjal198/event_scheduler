from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Task

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