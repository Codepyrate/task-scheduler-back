from django.urls import path
from .views import *

urlpatterns = [
    path("/notes", NoteList.as_view(), name="note_list"), 
    path("<int:pk>/", NoteDetail.as_view(), name="note_detail"),
    # task 
    path("/tasks", TaskList.as_view(), name="task_list"),
    path("<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    # create user
    # path("create-user/", user_creation(), name="user_create"),
]