from django.db.models import query
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView
# test1
from django.shortcuts import render

from .models import Task
from .serializers import TaskSerlizer
# Create your views here.

class TaskListView(ListCreateAPIView):
    queryset= Task.objects.all()
    serializer_class = TaskSerlizer
    
class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerlizer
    
class TaskUpdate(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerlizer


  