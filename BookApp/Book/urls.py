from django.contrib import admin
from django.urls import path
from Book import views

urlpatterns = [
    path('', views.read,name = "index")
]