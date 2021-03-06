from django.db import models
from django.contrib.auth import get_user_model



class Note(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    message = models.TextField() 
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return self.title

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    message = models.TextField() 
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self) :
        return self.title

    


    

