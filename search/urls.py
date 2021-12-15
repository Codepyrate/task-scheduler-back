from django.urls import path
from .views import get_query
from .views import *




urlpatterns =[

path('' , get_query , name="search")
]