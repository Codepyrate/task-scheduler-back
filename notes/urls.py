from django.urls import path
from rest_framework import views
from .views import *

urlpatterns = [
    path("notes", NoteList.as_view(), name="note_list"), 
    path("note/<int:pk>/", NoteDetail.as_view(), name="note_detail"),
    # task 
    path("tasks", TaskList.as_view(), name="task_list"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    #user
    path("users", UserList.as_view(), name="user_list"), 
    path("user/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    
]