from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, AEROCLUB, ASTROCLUB, CACLUB, EECLUB, PRAKRITICLUB, FNCCLUB, ROBOTICSCLUB, EDCLUB, UGCLUB, \
    ALCHERCLUB, TechnicheCLUB, OTHERCLUB, SAILCLUB, AICLUB, CCDCLUB
from .models import BT, CH, CL, CE, CSE, DES, ECE, EEE, MA, ME, PH, CODINGCLUB, SWC
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .aserializer import TaskSerializer
from .serializer import BTSerializer, CHSerializer, CLSerializer, CESerializer, CSESerializer, DESSerializer, \
    ECESerializer, EEESerializer, MASerializer, MESerializer, PHSerializer, CODINGCLUBSerializer, SWCSerializer, \
    AEROCLUBSerializer, ASTROCLUBSerializer, CACLUBSerializer, EECLUBSerializer, PRAKRITICLUBSerializer, \
    FNCCLUBSerializer, ROBOTICSCLUBSerializer, EDCLUBSerializer, UGCLUBSerializer, ALCHERSerializer, \
    TechnicheSerializer, OTHERSerializer, SAILSerializer, AISerializer, CCDSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework import generics, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import django_filters.rest_framework


# Create your views here.
def index(request):
    param = {
        'tasks': Task.objects.all()
    }
    return render(request, 'tasks/index.html', param)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = ['date']


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'event_type', 'target_batch', 'target_branch', 'date', 'time_from', 'time_to', 'remainder',
              'remainder_date', 'remainder_time', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'event_type', 'target_batch', 'target_branch', 'date', 'time_from', 'time_to', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False


class TaskDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False


def TASKSEE(request, pk):
    stu = Task.objects.get(id=pk)
    serializer = TaskSerializer(stu)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)


# @csrf_exempt
# def CREATETASK(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#
#         pythondata = JSONParser().parse(stream)
#
#         serializer = TaskDSerializer(data=pythondata)
#
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'created'}
#             json_data = JSONRenderer().render(res)
#
#             return HttpResponse(json_data, content_type='application/json')
#     json_data = JSONRenderer().render(serializer.errors)
#     return HttpResponse(json_data, content_type='application/json')


class TaskListAPI(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Task.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class TaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class BTTaskListAPI(generics.ListAPIView):
    serializer_class = BTSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = BT.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class BTTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BTSerializer
    queryset = BT.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class BTTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = BTSerializer
    queryset = BT.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class CHTaskListAPI(generics.ListAPIView):
    serializer_class = CHSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CH.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class CHTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CHSerializer
    queryset = CH.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class CHTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CHSerializer
    queryset = CH.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class CLTaskListAPI(generics.ListAPIView):
    serializer_class = CLSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CL.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class CLTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CLSerializer
    queryset = CL.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class CLTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CLSerializer
    queryset = CL.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class CETaskListAPI(generics.ListAPIView):
    serializer_class = CESerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class CETaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CESerializer
    queryset = CE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class CETaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CESerializer
    queryset = CE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class CSETaskListAPI(generics.ListAPIView):
    serializer_class = CSESerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CSE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class CSETaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CSESerializer
    queryset = CSE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class CSETaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CSESerializer
    queryset = CSE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class DESTaskListAPI(generics.ListAPIView):
    serializer_class = DESSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = DES.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class DESTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DESSerializer
    queryset = DES.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class DESTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = DESSerializer
    queryset = DES.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class ECETaskListAPI(generics.ListAPIView):
    serializer_class = ECESerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ECE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class ECETaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ECESerializer
    queryset = ECE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class ECETaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = ECESerializer
    queryset = ECE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class EEETaskListAPI(generics.ListAPIView):
    serializer_class = EEESerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EEE.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class EEETaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EEESerializer
    queryset = EEE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class EEETaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = EEESerializer
    queryset = EEE.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class MATaskListAPI(generics.ListAPIView):
    serializer_class = MASerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = MA.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class MATaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MASerializer
    queryset = MA.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class MATaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = MASerializer
    queryset = MA.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class METaskListAPI(generics.ListAPIView):
    serializer_class = MESerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ME.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class METaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MESerializer
    queryset = ME.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class METaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = MESerializer
    queryset = ME.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class PHTaskListAPI(generics.ListAPIView):
    serializer_class = PHSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PH.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class PHTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PHSerializer
    queryset = PH.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class PHTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = PHSerializer
    queryset = PH.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class SWCTaskListAPI(generics.ListAPIView):
    serializer_class = SWCSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = SWC.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class SWCTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SWCSerializer
    queryset = SWC.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class SWCTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = SWCSerializer
    queryset = SWC.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class CODINGCLUBTaskListAPI(generics.ListAPIView):
    serializer_class = CODINGCLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CODINGCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class CODINGCLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CODINGCLUBSerializer
    queryset = CODINGCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class CODINGCLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CODINGCLUBSerializer
    queryset = CODINGCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class AEROCLUBTaskListAPI(generics.ListAPIView):
    serializer_class = AEROCLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = AEROCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class AEROCLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AEROCLUBSerializer
    queryset = AEROCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class AEROCLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = AEROCLUBSerializer
    queryset = AEROCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class ASTROCLUBTaskListAPI(generics.ListAPIView):
    serializer_class = ASTROCLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ASTROCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class ASTROCLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ASTROCLUBSerializer
    queryset = ASTROCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class ASTROCLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = ASTROCLUBSerializer
    queryset = ASTROCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class CACLUBTaskListAPI(generics.ListAPIView):
    serializer_class = CACLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CACLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class CACLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CACLUBSerializer
    queryset = CACLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class CACLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CACLUBSerializer
    queryset = CACLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class EECLUBTaskListAPI(generics.ListAPIView):
    serializer_class = EECLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EECLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class EECLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EECLUBSerializer
    queryset = EECLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class EECLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = EECLUBSerializer
    queryset = EECLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class PRAKRITICLUBTaskListAPI(generics.ListAPIView):
    serializer_class = PRAKRITICLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = PRAKRITICLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class PRAKRITICLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PRAKRITICLUBSerializer
    queryset = PRAKRITICLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class PRAKRITICLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = PRAKRITICLUBSerializer
    queryset = PRAKRITICLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class FNCCLUBTaskListAPI(generics.ListAPIView):
    serializer_class = FNCCLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = FNCCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class FNCCLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FNCCLUBSerializer
    queryset = FNCCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class FNCCLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = FNCCLUBSerializer
    queryset = FNCCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class ROBOTICSCLUBTaskListAPI(generics.ListAPIView):
    serializer_class = ROBOTICSCLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ROBOTICSCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class ROBOTICSCLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ROBOTICSCLUBSerializer
    queryset = ROBOTICSCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class ROBOTICSCLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = ROBOTICSCLUBSerializer
    queryset = ROBOTICSCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class EDCLUBTaskListAPI(generics.ListAPIView):
    serializer_class = EDCLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = EDCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class EDCLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EDCLUBSerializer
    queryset = EDCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class EDCLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = EDCLUBSerializer
    queryset = EDCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class UGCLUBTaskListAPI(generics.ListAPIView):
    serializer_class = UGCLUBSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = UGCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class UGCLUBTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UGCLUBSerializer
    queryset = UGCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class UGCLUBTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = UGCLUBSerializer
    queryset = UGCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class ALCHERTaskListAPI(generics.ListAPIView):
    serializer_class = ALCHERSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ALCHERCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class ALCHERTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ALCHERSerializer
    queryset = ALCHERCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class ALCHERTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = ALCHERSerializer
    queryset = ALCHERCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class TechnicheTaskListAPI(generics.ListAPIView):
    serializer_class = TechnicheSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = TechnicheCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class TechnicheTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TechnicheSerializer
    queryset = TechnicheCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class TechnicheTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = TechnicheSerializer
    queryset = TechnicheCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class OTHERTaskListAPI(generics.ListAPIView):
    serializer_class = OTHERSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = OTHERCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class OTHERTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OTHERSerializer
    queryset = OTHERCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class OTHERTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = OTHERSerializer
    queryset = OTHERCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class SAILTaskListAPI(generics.ListAPIView):
    serializer_class = SAILSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = SAILCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class SAILTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SAILSerializer
    queryset = SAILCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class SAILTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = SAILSerializer
    queryset = SAILCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class AITaskListAPI(generics.ListAPIView):
    serializer_class = AISerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = AICLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class AITaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AISerializer
    queryset = AICLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class AITaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = AISerializer
    queryset = AICLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)


class CCDTaskListAPI(generics.ListAPIView):
    serializer_class = CCDSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CCDCLUB.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title', 'description', 'author__name')


class CCDTaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CCDSerializer
    queryset = CCDCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)


class CCDTaskCreateAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CCDSerializer
    queryset = CCDCLUB.objects.all()
    permission_class = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request):
        return self.create(request)



def task(request):
    return render(request, 'tasks/TaskView.html')


def acad(request):
    return render(request, 'tasks/branchAC.html')


def club(request):
    return render(request, 'tasks/clubs.html')


def occ(request):
    return render(request, 'tasks/ocaasional.html')


def cal(request):
    return render(request, 'tasks/calendar.html')


def org(request):
    return render(request, 'tasks/organisation.html')







