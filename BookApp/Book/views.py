from django.shortcuts import render,redirect
from .models import Book
from django.urls import reverse_lazy

# Create your views here.
def read(request):
    books = Book.objects.all()
    context = {"book":books}
    return render (request,"Book/book_list.html",context)

def create(request):
    pass

def update(request):
    pass

def delete(request):
    pass