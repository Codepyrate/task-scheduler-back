from django.urls import path
from .views import get_query




urlpatterns =[

path('' , get_query , name="search")
]