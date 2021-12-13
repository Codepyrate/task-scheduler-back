from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    message = models.TextField() 
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def str(self) :
        return self.title