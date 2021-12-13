from django.db import models
from django.contrib.auth import get_user_model
class Task():
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=64)
    message = models.TextField() 
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()
    
    def __str__(self) :
        return self.title
