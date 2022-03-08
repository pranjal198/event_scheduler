from django.urls import path
from .views import ClubListView
from . import views


urlpatterns = [
    path('event-scheduler/',ClubListView.as_view(),name='clubs-home'),
    path('<int:pk>/', views.ClubListView.as_view()),
]