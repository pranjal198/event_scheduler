from django.urls import path
from .views import TaskListView,TaskDetailView,TaskCreateView,TaskUpdateView,TaskDeleteView,TaskListAPI,TaskDetailAPI,TaskCreateAPI
from . import views

urlpatterns = [
    path('',TaskListView.as_view(),name='tasks-home'),
    path('task/<int:pk>/',TaskDetailView.as_view(),name='tasks-detail'),
    path('task/<int:pk>/update/',TaskUpdateView.as_view(),name='tasks-update'),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(),name='tasks-delete'),
    path('task/new/',TaskCreateView.as_view(),name='tasks-create'),
    path('API',TaskListAPI.as_view(),name='tasks-list'),
    path('API/<int:pk>/',TaskDetailAPI.as_view(),name='tasks-detail'),
    path('API/new/',TaskCreateAPI.as_view(),name='tasks-create'),

]
