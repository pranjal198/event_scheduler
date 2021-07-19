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
from users import views as user_views
from django.contrib.auth import views as auth_views
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('tasks.urls')),
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('alltask/<int:pk>/',views.TASKSEE),
    # path("createtask/",views.CREATETASK),
    path('API/', views.TaskListAPI.as_view(), name='tasks-list'),
    path('API/<int:pk>/', views.TaskDetailAPI.as_view(), name='tasks-detail'),
    path('API/new/', views.TaskCreateAPI.as_view(), name='tasks-create'),

    path('BTAPI/', views.BTTaskListAPI.as_view(), name='tasks-list'),
    path('BTAPI/<int:pk>/', views.BTTaskDetailAPI.as_view(), name='tasks-detail'),
    path('BTAPI/new/', views.BTTaskCreateAPI.as_view(), name='tasks-create'),

    path('CHAPI/', views.CHTaskListAPI.as_view(), name='tasks-list'),
    path('CHAPI/<int:pk>/', views.CHTaskDetailAPI.as_view(), name='tasks-detail'),
    path('CHAPI/new/', views.CHTaskCreateAPI.as_view(), name='tasks-create'),

    path('CLAPI/', views.CLTaskListAPI.as_view(), name='tasks-list'),
    path('CLAPI/<int:pk>/', views.CLTaskDetailAPI.as_view(), name='tasks-detail'),
    path('CLAPI/new/', views.CLTaskCreateAPI.as_view(), name='tasks-create'),

    path('CEAPI/', views.CETaskListAPI.as_view(), name='tasks-list'),
    path('CEAPI/<int:pk>/', views.CETaskDetailAPI.as_view(), name='tasks-detail'),
    path('CEAPI/new/', views.CETaskCreateAPI.as_view(), name='tasks-create'),

    path('CSEAPI/', views.CSETaskListAPI.as_view(), name='tasks-list'),
    path('CSEAPI/<int:pk>/', views.CSETaskDetailAPI.as_view(), name='tasks-detail'),
    path('CSEAPI/new/', views.CSETaskCreateAPI.as_view(), name='tasks-create'),

    path('DESAPI/', views.DESTaskListAPI.as_view(), name='tasks-list'),
    path('DESAPI/<int:pk>/', views.DESTaskDetailAPI.as_view(), name='tasks-detail'),
    path('DESAPI/new/', views.DESTaskCreateAPI.as_view(), name='tasks-create'),

    path('ECEAPI/', views.ECETaskListAPI.as_view(), name='tasks-list'),
    path('ECEAPI/<int:pk>/', views.ECETaskDetailAPI.as_view(), name='tasks-detail'),
    path('ECEAPI/new/', views.ECETaskCreateAPI.as_view(), name='tasks-create'),

    path('EEEAPI/', views.EEETaskListAPI.as_view(), name='tasks-list'),
    path('EEEAPI/<int:pk>/', views.EEETaskDetailAPI.as_view(), name='tasks-detail'),
    path('EEEPI/new/', views.EEETaskCreateAPI.as_view(), name='tasks-create'),

    path('MAAPI/', views.MATaskListAPI.as_view(), name='tasks-list'),
    path('MAAPI/<int:pk>/', views.MATaskDetailAPI.as_view(), name='tasks-detail'),
    path('MAAPI/new/', views.MATaskCreateAPI.as_view(), name='tasks-create'),

    path('MEAPI/', views.METaskListAPI.as_view(), name='tasks-list'),
    path('MEAPI/<int:pk>/', views.METaskDetailAPI.as_view(), name='tasks-detail'),
    path('MEAPI/new/', views.METaskCreateAPI.as_view(), name='tasks-create'),

    path('PHAPI/', views.PHTaskListAPI.as_view(), name='tasks-list'),
    path('PHAPI/<int:pk>/', views.PHTaskDetailAPI.as_view(), name='tasks-detail'),
    path('PHAPI/new/', views.PHTaskCreateAPI.as_view(), name='tasks-create'),


    path('SWCAPI/', views.SWCTaskListAPI.as_view(), name='tasks-list'),
    path('SWCAPI/<int:pk>/', views.SWCTaskDetailAPI.as_view(), name='tasks-detail'),
    path('SWCAPI/new/', views.SWCTaskCreateAPI.as_view(), name='tasks-create'),

    path('CDCLUBAPI/', views.CODINGCLUBTaskListAPI.as_view(), name='tasks-list'),
    path('CDCLUBAPI/<int:pk>/', views.CODINGCLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('CDCLUBAPI/new/', views.CODINGCLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('AEROCLUBAPI/', views.AEROCLUBTaskListAPI.as_view(), name='tasks-list'),
    path('AEROCLUBAPI/<int:pk>/', views.AEROCLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('AEROCLUBAPI/new/', views.AEROCLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('ASTROCLUBAPI/', views.ASTROCLUBTaskListAPI.as_view(), name='tasks-list'),
    path('ASTROCLUBAPI/<int:pk>/', views.ASTROCLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('ASTROCLUBAPI/new/', views.ASTROCLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('CACLUBAPI/', views.CACLUBTaskListAPI.as_view(), name='tasks-list'),
    path('CACLUBAPI/<int:pk>/', views.CACLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('CACLUBAPI/new/', views.CACLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('EECLUBAPI/', views.EECLUBTaskListAPI.as_view(), name='tasks-list'),
    path('EECLUBAPI/<int:pk>/', views.EECLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('EECLUBAPI/new/', views.EECLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('PRAKRITICLUBAPI/', views.PRAKRITICLUBTaskListAPI.as_view(), name='tasks-list'),
    path('PRAKRITICLUBAPI/<int:pk>/', views.PRAKRITICLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('PRAKRITICLUBAPI/new/', views.PRAKRITICLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('FNCCLUBAPI/', views.FNCCLUBTaskListAPI.as_view(), name='tasks-list'),
    path('FNCCLUBAPI/<int:pk>/', views.FNCCLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('FNCCLUBAPI/new/', views.FNCCLUBTaskCreateAPI.as_view(), name='tasks-create'),


    path('ROBOTICSCLUBAPI/', views.ROBOTICSCLUBTaskListAPI.as_view(), name='tasks-list'),
    path('ROBOTICSCLUBAPI/<int:pk>/', views.ROBOTICSCLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('ROBOTICSCLUBAPI/new/', views.ROBOTICSCLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('EDCLUBAPI/', views.EDCLUBTaskListAPI.as_view(), name='tasks-list'),
    path('EDCLUBAPI/<int:pk>/', views.EDCLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('EDCLUBAPI/new/', views.EDCLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('UGCLUBAPI/', views.UGCLUBTaskListAPI.as_view(), name='tasks-list'),
    path('UGCLUBAPI/<int:pk>/', views.UGCLUBTaskDetailAPI.as_view(), name='tasks-detail'),
    path('UGCLUBAPI/new/', views.UGCLUBTaskCreateAPI.as_view(), name='tasks-create'),

    path('ALCHERCLUBAPI/', views.ALCHERTaskListAPI.as_view(), name='tasks-list'),
    path('ALCHERCLUBAPI/<int:pk>/', views.ALCHERTaskDetailAPI.as_view(), name='tasks-detail'),
    path('ALCHERCLUBAPI/new/', views.ALCHERTaskCreateAPI.as_view(), name='tasks-create'),


    path('TECHNICHECLUBAPI/', views.TechnicheTaskListAPI.as_view(), name='tasks-list'),
    path('TECHNICHECLUBAPI/<int:pk>/', views.TechnicheTaskDetailAPI.as_view(), name='tasks-detail'),
    path('TECHNICHECLUBAPI/new/', views.TechnicheTaskCreateAPI.as_view(), name='tasks-create'),


    path('OTHERCLUBAPI/', views.OTHERTaskListAPI.as_view(), name='tasks-list'),
    path('OTHERCLUBAPI/<int:pk>/', views.OTHERTaskDetailAPI.as_view(), name='tasks-detail'),
    path('OTHERCLUBAPI/new/', views.OTHERTaskCreateAPI.as_view(), name='tasks-create'),


    path('SAILCLUBAPI/', views.SAILTaskListAPI.as_view(), name='tasks-list'),
    path('SAILCLUBAPI/<int:pk>/', views.SAILTaskDetailAPI.as_view(), name='tasks-detail'),
    path('SAILCLUBAPI/new/', views.SAILTaskCreateAPI.as_view(), name='tasks-create'),

    path('AICLUBAPI/', views.AITaskListAPI.as_view(), name='tasks-list'),
    path('AICLUBAPI/<int:pk>/', views.AITaskDetailAPI.as_view(), name='tasks-detail'),
    path('AICLUBAPI/new/', views.AITaskCreateAPI.as_view(), name='tasks-create'),

    path('CCDCLUBAPI/', views.CCDTaskListAPI.as_view(), name='tasks-list'),
    path('CCDCLUBAPI/<int:pk>/', views.CCDTaskDetailAPI.as_view(), name='tasks-detail'),
    path('CCDCLUBAPI/new/', views.CCDTaskCreateAPI.as_view(), name='tasks-create'),
]
