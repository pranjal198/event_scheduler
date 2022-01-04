from django.urls import path
from .views import TaskListView
from . import views


urlpatterns = [
    path('',TaskListView.as_view(),name='tasks-home'),
    path('<int:pk>/', views.TaskListView.as_view()),
]

