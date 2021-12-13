   
from django.urls import path
from .views import (TaskListView,
                    TaskDetail,
                    TaskUpdate
                    )

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),
]