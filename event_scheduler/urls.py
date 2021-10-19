from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from tasks import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('alltask/<int:pk>/', views.TASKSEE),
    # path("createtask/",views.CREATETASK),
    path('API/', views.TaskListAPI.as_view(), name='tasks-list'),
    path('API/<int:pk>/', views.TaskDetailAPI.as_view(), name='tasks-detail'),
    path('API/new/', views.TaskCreateAPI.as_view(), name='tasks-create'),

    path('BTAPI/', views.BTTaskListAPI.as_view(), name='bt-list'),
    path('BTAPI/<int:pk>/', views.BTTaskDetailAPI.as_view(), name='bt-detail'),
    path('BTAPI/new/', views.BTTaskCreateAPI.as_view(), name='tasks-create'),

    path('CHAPI/', views.CHTaskListAPI.as_view(), name='ch-list'),
    path('CHAPI/<int:pk>/', views.CHTaskDetailAPI.as_view(), name='ch-detail'),
    path('CHAPI/new/', views.CHTaskCreateAPI.as_view(), name='tasks-create'),

    path('CLAPI/', views.CLTaskListAPI.as_view(), name='cl-list'),
    path('CLAPI/<int:pk>/', views.CLTaskDetailAPI.as_view(), name='cl-detail'),
    path('CLAPI/new/', views.CLTaskCreateAPI.as_view(), name='tasks-create'),

    path('CEAPI/', views.CETaskListAPI.as_view(), name='ce-list'),
    path('CEAPI/<int:pk>/', views.CETaskDetailAPI.as_view(), name='ce-detail'),
    path('CEAPI/new/', views.CETaskCreateAPI.as_view(), name='ce-create'),

    path('CSEAPI/', views.CSETaskListAPI.as_view(), name='cse-list'),
    path('CSEAPI/<int:pk>/', views.CSETaskDetailAPI.as_view(), name='cse-detail'),
    path('CSEAPI/new/', views.CSETaskCreateAPI.as_view(), name='cse-create'),

    path('DESAPI/', views.DESTaskListAPI.as_view(), name='des-list'),
    path('DESAPI/<int:pk>/', views.DESTaskDetailAPI.as_view(), name='des-detail'),
    path('DESAPI/new/', views.DESTaskCreateAPI.as_view(), name='des-create'),

    path('ECEAPI/', views.ECETaskListAPI.as_view(), name='ece-list'),
    path('ECEAPI/<int:pk>/', views.ECETaskDetailAPI.as_view(), name='ece-detail'),
    path('ECEAPI/new/', views.ECETaskCreateAPI.as_view(), name='ece-create'),

    path('EEEAPI/', views.EEETaskListAPI.as_view(), name='eee-list'),
    path('EEEAPI/<int:pk>/', views.EEETaskDetailAPI.as_view(), name='eee-detail'),
    path('EEEPI/new/', views.EEETaskCreateAPI.as_view(), name='eee-create'),

    path('MAAPI/', views.MATaskListAPI.as_view(), name='ma-list'),
    path('MAAPI/<int:pk>/', views.MATaskDetailAPI.as_view(), name='ma-detail'),
    path('MAAPI/new/', views.MATaskCreateAPI.as_view(), name='ma-create'),

    path('MEAPI/', views.METaskListAPI.as_view(), name='me-list'),
    path('MEAPI/<int:pk>/', views.METaskDetailAPI.as_view(), name='me-detail'),
    path('MEAPI/new/', views.METaskCreateAPI.as_view(), name='me-create'),

    path('PHAPI/', views.PHTaskListAPI.as_view(), name='ph-list'),
    path('PHAPI/<int:pk>/', views.PHTaskDetailAPI.as_view(), name='ph-detail'),
    path('PHAPI/new/', views.PHTaskCreateAPI.as_view(), name='ph-create'),


    path('SWCAPI/', views.SWCTaskListAPI.as_view(), name='swc-list'),
    path('SWCAPI/<int:pk>/', views.SWCTaskDetailAPI.as_view(), name='swc-detail'),
    path('SWCAPI/new/', views.SWCTaskCreateAPI.as_view(), name='swc-create'),

    path('CDCLUBAPI/', views.CODINGCLUBTaskListAPI.as_view(), name='codingclub-list'),
    path('CDCLUBAPI/<int:pk>/', views.CODINGCLUBTaskDetailAPI.as_view(),
         name='codingclub-detail'),
    path('CDCLUBAPI/new/', views.CODINGCLUBTaskCreateAPI.as_view(),
         name='codingclub-create'),

    path('AEROCLUBAPI/', views.AEROCLUBTaskListAPI.as_view(), name='aeroclub-list'),
    path('AEROCLUBAPI/<int:pk>/',
         views.AEROCLUBTaskDetailAPI.as_view(), name='aeroclub-detail'),
    path('AEROCLUBAPI/new/', views.AEROCLUBTaskCreateAPI.as_view(),
         name='aeroclub-create'),

    path('ASTROCLUBAPI/', views.ASTROCLUBTaskListAPI.as_view(),
         name='astroclub-list'),
    path('ASTROCLUBAPI/<int:pk>/',
         views.ASTROCLUBTaskDetailAPI.as_view(), name='astroclub-detail'),
    path('ASTROCLUBAPI/new/', views.ASTROCLUBTaskCreateAPI.as_view(),
         name='astroclub-create'),

    path('CACLUBAPI/', views.CACLUBTaskListAPI.as_view(), name='caclub-list'),
    path('CACLUBAPI/<int:pk>/',
         views.CACLUBTaskDetailAPI.as_view(), name='caclub-detail'),
    path('CACLUBAPI/new/', views.CACLUBTaskCreateAPI.as_view(), name='caclub-create'),

    path('EECLUBAPI/', views.EECLUBTaskListAPI.as_view(), name='eeclub-list'),
    path('EECLUBAPI/<int:pk>/',
         views.EECLUBTaskDetailAPI.as_view(), name='eeclub-detail'),
    path('EECLUBAPI/new/', views.EECLUBTaskCreateAPI.as_view(), name='eeclub-create'),

    path('PRAKRITICLUBAPI/', views.PRAKRITICLUBTaskListAPI.as_view(),
         name='prakriticlub-list'),
    path('PRAKRITICLUBAPI/<int:pk>/',
         views.PRAKRITICLUBTaskDetailAPI.as_view(), name='prakriticlub-detail'),
    path('PRAKRITICLUBAPI/new/', views.PRAKRITICLUBTaskCreateAPI.as_view(),
         name='prakriticlub-create'),

    path('FNCCLUBAPI/', views.FNCCLUBTaskListAPI.as_view(), name='fncclub-list'),
    path('FNCCLUBAPI/<int:pk>/',
         views.FNCCLUBTaskDetailAPI.as_view(), name='fncclub-detail'),
    path('FNCCLUBAPI/new/', views.FNCCLUBTaskCreateAPI.as_view(),
         name='fncclub-create'),


    path('ROBOTICSCLUBAPI/', views.ROBOTICSCLUBTaskListAPI.as_view(),
         name='roboticsclub-list'),
    path('ROBOTICSCLUBAPI/<int:pk>/',
         views.ROBOTICSCLUBTaskDetailAPI.as_view(), name='roboticsclub-detail'),
    path('ROBOTICSCLUBAPI/new/', views.ROBOTICSCLUBTaskCreateAPI.as_view(),
         name='roboticsclub-create'),

    path('EDCLUBAPI/', views.EDCLUBTaskListAPI.as_view(), name='edclub-list'),
    path('EDCLUBAPI/<int:pk>/',
         views.EDCLUBTaskDetailAPI.as_view(), name='edclub-detail'),
    path('EDCLUBAPI/new/', views.EDCLUBTaskCreateAPI.as_view(), name='edclub-create'),

    path('UGCLUBAPI/', views.UGCLUBTaskListAPI.as_view(), name='ugclub-list'),
    path('UGCLUBAPI/<int:pk>/',
         views.UGCLUBTaskDetailAPI.as_view(), name='ugclub-detail'),
    path('UGCLUBAPI/new/', views.UGCLUBTaskCreateAPI.as_view(), name='ugclub-create'),

    path('ALCHERCLUBAPI/', views.ALCHERTaskListAPI.as_view(), name='alcherclub-list'),
    path('ALCHERCLUBAPI/<int:pk>/',
         views.ALCHERTaskDetailAPI.as_view(), name='alcherclub-detail'),
    path('ALCHERCLUBAPI/new/', views.ALCHERTaskCreateAPI.as_view(),
         name='alcherclub-create'),


    path('TECHNICHECLUBAPI/', views.TechnicheTaskListAPI.as_view(),
         name='technicheclub-list'),
    path('TECHNICHECLUBAPI/<int:pk>/',
         views.TechnicheTaskDetailAPI.as_view(), name='tehnicheclub-detail'),
    path('TECHNICHECLUBAPI/new/', views.TechnicheTaskCreateAPI.as_view(),
         name='tehnicheclub-create'),


    path('OTHERCLUBAPI/', views.OTHERTaskListAPI.as_view(), name='otherclub-list'),
    path('OTHERCLUBAPI/<int:pk>/',
         views.OTHERTaskDetailAPI.as_view(), name='otherclub-detail'),
    path('OTHERCLUBAPI/new/', views.OTHERTaskCreateAPI.as_view(),
         name='otherclub-create'),


    path('SAILCLUBAPI/', views.SAILTaskListAPI.as_view(), name='sailclub-list'),
    path('SAILCLUBAPI/<int:pk>/',
         views.SAILTaskDetailAPI.as_view(), name='sailclub-detail'),
    path('SAILCLUBAPI/new/', views.SAILTaskCreateAPI.as_view(),
         name='sailclub-create'),

    path('AICLUBAPI/', views.AITaskListAPI.as_view(), name='aiclub-list'),
    path('AICLUBAPI/<int:pk>/', views.AITaskDetailAPI.as_view(), name='aiclub-detail'),
    path('AICLUBAPI/new/', views.AITaskCreateAPI.as_view(), name='aiclub-create'),

    path('CCDCLUBAPI/', views.CCDTaskListAPI.as_view(), name='ccdclub-list'),
    path('CCDCLUBAPI/<int:pk>/',
         views.CCDTaskDetailAPI.as_view(), name='ccdclub-detail'),
    path('CCDCLUBAPI/new/', views.CCDTaskCreateAPI.as_view(), name='ccdclub-create'),

    # RSVP API's

    path('RSVP/AEROCLUB/', user_views.Rsvp_AEROCLUB_List_API.as_view(),
         name='rsvp-AEROCLUB-list'),
    path('RSVP/AEROCLUB/<int:pk>', user_views.Rsvp_AEROCLUB_Detail_API.as_view(),
         name='rsvp-AEROCLUB-detail'),

    path('RSVP/AICLUB/', user_views.Rsvp_AICLUB_List_API.as_view(),
         name='rsvp-AICLUB-list'),
    path('RSVP/AICLUB/<int:pk>', user_views.Rsvp_AICLUB_Detail_API.as_view(),
         name='rsvp-AICLUB-detail'),

    path('RSVP/ALCHERCLUB/', user_views.Rsvp_ALCHERCLUB_List_API.as_view(),
         name='rsvp-ALCHERCLUB-list'),
    path('RSVP/ALCHERCLUB/<int:pk>', user_views.Rsvp_ALCHERCLUB_Detail_API.as_view(),
         name='rsvp-ALCHERCLUB-detail'),

    path('RSVP/ASTROCLUB/', user_views.Rsvp_ASTROCLUB_List_API.as_view(),
         name='rsvp-ASTROCLUB-list'),
    path('RSVP/ASTROCLUB/<int:pk>', user_views.Rsvp_ASTROCLUB_Detail_API.as_view(),
         name='rsvp-ASTROCLUB-detail'),

    path('RSVP/BT/', user_views.Rsvp_BT_List_API.as_view(), name='rsvp-BT-list'),
    path('RSVP/BT/<int:pk>', user_views.Rsvp_BT_Detail_API.as_view(),
         name='rsvp-BT-detail'),

    path('RSVP/CACLUB/', user_views.Rsvp_CACLUB_List_API.as_view(),
         name='rsvp-CACLUB-list'),
    path('RSVP/CACLUB/<int:pk>', user_views.Rsvp_CACLUB_Detail_API.as_view(),
         name='rsvp-CACLUB-detail'),

    path('RSVP/CCDCLUB/', user_views.Rsvp_CCDCLUB_List_API.as_view(),
         name='rsvp-CCDCLUB-list'),
    path('RSVP/CCDCLUB/<int:pk>', user_views.Rsvp_CCDCLUB_Detail_API.as_view(),
         name='rsvp-CCDCLUB-detail'),

    path('RSVP/CE/', user_views.Rsvp_CE_List_API.as_view(), name='rsvp-CE-list'),
    path('RSVP/CE/<int:pk>', user_views.Rsvp_CE_Detail_API.as_view(),
         name='rsvp-CE-detail'),

    path('RSVP/CH/', user_views.Rsvp_CH_List_API.as_view(), name='rsvp-CH-list'),
    path('RSVP/CH/<int:pk>', user_views.Rsvp_CH_Detail_API.as_view(),
         name='rsvp-CH-detail'),

    path('RSVP/CL/', user_views.Rsvp_CL_List_API.as_view(), name='rsvp-CL-list'),
    path('RSVP/CL/<int:pk>', user_views.Rsvp_CL_Detail_API.as_view(),
         name='rsvp-CL-detail'),

    path('RSVP/CODINGCLUB/', user_views.Rsvp_CODINGCLUB_List_API.as_view(),
         name='rsvp-CODINGCLUB-list'),
    path('RSVP/CODINGCLUB/<int:pk>', user_views.Rsvp_CODINGCLUB_Detail_API.as_view(),
         name='rsvp-CODINGCLUB-detail'),

    path('RSVP/CSE/', user_views.Rsvp_CSE_List_API.as_view(), name='rsvp-CSE-list'),
    path('RSVP/CSE/<int:pk>', user_views.Rsvp_CSE_Detail_API.as_view(),
         name='rsvp-CSE-detail'),

    path('RSVP/DES/', user_views.Rsvp_DES_List_API.as_view(), name='rsvp-DES-list'),
    path('RSVP/DES/<int:pk>', user_views.Rsvp_DES_Detail_API.as_view(),
         name='rsvp-DES-detail'),

    path('RSVP/ECE/', user_views.Rsvp_ECE_List_API.as_view(), name='rsvp-ECE-list'),
    path('RSVP/ECE/<int:pk>', user_views.Rsvp_ECE_Detail_API.as_view(),
         name='rsvp-ECE-detail'),

    path('RSVP/EDCLUB/', user_views.Rsvp_EDCLUB_List_API.as_view(),
         name='rsvp-EDCLUB-list'),
    path('RSVP/EDCLUB/<int:pk>', user_views.Rsvp_EDCLUB_Detail_API.as_view(),
         name='rsvp-EDCLUB-detail'),

    path('RSVP/EECLUB/', user_views.Rsvp_EECLUB_List_API.as_view(),
         name='rsvp-EECLUB-list'),
    path('RSVP/EECLUB/<int:pk>', user_views.Rsvp_EECLUB_Detail_API.as_view(),
         name='rsvp-EECLUB-detail'),

    path('RSVP/EEE/', user_views.Rsvp_EEE_List_API.as_view(), name='rsvp-EEE-list'),
    path('RSVP/EEE/<int:pk>', user_views.Rsvp_EEE_Detail_API.as_view(),
         name='rsvp-EEE-detail'),

    path('RSVP/FNCCLUB/', user_views.Rsvp_FNCCLUB_List_API.as_view(),
         name='rsvp-FNCCLUB-list'),
    path('RSVP/FNCCLUB/<int:pk>', user_views.Rsvp_FNCCLUB_Detail_API.as_view(),
         name='rsvp-FNCCLUB-detail'),

    path('RSVP/MA/', user_views.Rsvp_MA_List_API.as_view(), name='rsvp-MA-list'),
    path('RSVP/MA/<int:pk>', user_views.Rsvp_MA_Detail_API.as_view(),
         name='rsvp-MA-detail'),

    path('RSVP/ME/', user_views.Rsvp_ME_List_API.as_view(), name='rsvp-ME-list'),
    path('RSVP/ME/<int:pk>', user_views.Rsvp_ME_Detail_API.as_view(),
         name='rsvp-ME-detail'),

    path('RSVP/OTHERCLUB/', user_views.Rsvp_OTHERCLUB_List_API.as_view(),
         name='rsvp-OTHERCLUB-list'),
    path('RSVP/OTHERCLUB/<int:pk>', user_views.Rsvp_OTHERCLUB_Detail_API.as_view(),
         name='rsvp-OTHERCLUB-detail'),

    path('RSVP/PH/', user_views.Rsvp_PH_List_API.as_view(), name='rsvp-PH-list'),
    path('RSVP/PH/<int:pk>', user_views.Rsvp_PH_Detail_API.as_view(),
         name='rsvp-PH-detail'),

    path('RSVP/PRAKRITICLUB/', user_views.Rsvp_PRAKRITICLUB_List_API.as_view(),
         name='rsvp-PRAKRITICLUB-list'),
    path('RSVP/PRAKRITICLUB/<int:pk>', user_views.Rsvp_PRAKRITICLUB_Detail_API.as_view(),
         name='rsvp-PRAKRITICLUB-detail'),

    path('RSVP/SAILCLUB/', user_views.Rsvp_SAILCLUB_List_API.as_view(),
         name='rsvp-SAILCLUB-list'),
    path('RSVP/SAILCLUB/<int:pk>', user_views.Rsvp_SAILCLUB_Detail_API.as_view(),
         name='rsvp-SAILCLUB-detail'),

    path('RSVP/SWC/', user_views.Rsvp_SWC_List_API.as_view(), name='rsvp-SWC-list'),
    path('RSVP/SWC/<int:pk>', user_views.Rsvp_SWC_Detail_API.as_view(),
         name='rsvp-SWC-detail'),

    path('RSVP/Task/', user_views.Rsvp_Task_List_API.as_view(),
         name='rsvp-Task-list'),
    path('RSVP/Task/<int:pk>', user_views.Rsvp_Task_Detail_API.as_view(),
         name='rsvp-Task-detail'),

    path('RSVP/Techniche/', user_views.Rsvp_TechnicheCLUB_List_API.as_view(),
         name='rsvp-Techniche-list'),
    path('RSVP/Techniche/<int:pk>', user_views.Rsvp_TechnicheCLUB_Detail_API.as_view(),
         name='rsvp-Techniche-detail'),

    path('RSVP/UGCLUB/', user_views.Rsvp_UGCLUB_List_API.as_view(),
         name='rsvp-UGCLUB-list'),
    path('RSVP/UGCLUB/<int:pk>', user_views.Rsvp_UGCLUB_Detail_API.as_view(),
         name='rsvp-UGCLUB-detail'),

    path('RSVP/ROBOTICSCLUB/', user_views.Rsvp_ROBOTICSCLUB_List_API.as_view(),
         name='rsvp-ROBOTICSCLUB-list'),
    path('RSVP/ROBOTICSCLUB/<int:pk>', user_views.Rsvp_ROBOTICSCLUB_Detail_API.as_view(),
         name='rsvp-ROBOTICSCLUB-detail'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
