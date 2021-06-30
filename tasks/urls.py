from django.urls import path
from .views import TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,TaskDeleteView
from . import views 

urlpatterns = [
    path('',TaskListView.as_view(),name='tasks-home'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='tasks-detail'),
    path('task/<int:pk>/update/',TaskUpdateView.as_view(),name='tasks-update'),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(),name='tasks-delete'),
    path('task/new/',TaskCreateView.as_view(),name='tasks-create'),

]