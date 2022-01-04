"""event_scheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from users import views as user_views
from django.contrib.auth import views as auth_views
from tasks import views
from rest_framework.schemas import get_schema_view


# schema_view = get_schema_view(
#    openapi.Info(
#       title="Snippets API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tasks.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('profile/',user_views.profile, name='profile'),

    path('api/tasks/',views.myTaskListAPI.as_view(),name='all-tasks'),
    path('api/tasks/<int:pk>/',views.myTaskDetailAPI.as_view(),name='one-tasks'),
    path('api/tasks/new/',views.myTaskCreateAPI.as_view(),name='new-task'),
    path('api/tasks/<int:pk>/update/',views.myTaskUpdateAPI.as_view(),name='edit-task'),

    path('profile/',user_views.get_profile,name='profile'),
    path('rsvp/all/',user_views.get_all_rsvp_tasks,name='rsvp-all'),
    path('rsvp/allother/',user_views.get_all_other_tasks,name='rsvp-all-other'),
    path('rsvp/allclub/<str:club_name>/',user_views.get_rsvp_club_tasks,name='rsvp-allclub'),
    path('rsvp/newclub/<str:club_name>/',user_views.get_new_club_tasks,name='rsvp-newclub'),


]

urlpatterns = urlpatterns+[

   path('openapi/', get_schema_view(
        title="TaskAPI",
        description="API's_FOR_TASK_CREATION"
    ), name='openapi-schema'),

    path('swagger/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
