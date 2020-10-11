from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import *
from .serializers import *
from pdb import set_trace


# Create your views here.
class UserView(ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskView(ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class BoardColumnView(ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = BoardColumn.objects.all()
    serializer_class = BoardColumnSerializer

class ProjectView(ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer