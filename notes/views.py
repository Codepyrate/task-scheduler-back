from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.permissions import AllowAny
from .models import Note,Task
from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer ,TaskSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_protect


class NoteList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class TaskList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


# print("hi")
# def my_cron_job():
#     print("Hello")
# 


# def create_new_user(data):   
#     user = User.objects.create_user(username=data['username'],email=data['email'],password=data['password'])
#     user.save()



# function for create a new user
# @api_view(['POST','GET'])
# @permission_classes((AllowAny,))
# def user_creation(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)