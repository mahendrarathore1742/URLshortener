from django.urls import path;
from .views import (Home,deshbord,generate)
urlpatterns = [
    path("",Home),
    path('deshbord/',deshbord,name='deshbord'),
    path('generate/',generate,name='generate'),
    path("<slug:slug>/" ,Home,name='Home'),
   
]
 