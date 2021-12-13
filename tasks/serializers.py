from rest_framework import serializers

from .models import Task

class TaskSerlizer(serializers.ModelSerializer):
    class Meta :
        model = Task
        fields = ('id', 'message' ,'title', 'date', 'time')