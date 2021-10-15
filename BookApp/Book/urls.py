from django.contrib import admin
from django.urls import path
from Book import views

urlpatterns = [
    path('', views.read,name = "index"),
    path('new/',views.create,name = "new")
]