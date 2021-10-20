from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import *
from django.http import *

# Create your views here.
def read(request):
    books = Book.objects.all()
    context = {"book":books}
    return render (request,"Book/book_list.html",context)

@csrf_protect
def create(request): 
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
           # book = Book()
           # book.title = form.cleaned_data["title"]
           # book.author = form.cleaned_data["author"]
            #book.comment = form.cleaned_data["comment"]
            form.save()
           # book.save()
            return HttpResponseRedirect('/')
        context = {"form":form}
        return render(request,"Book/book_create.html",context)


def detail_view(request,id):
    book = Book.objects.get(id = id)
    context = {"object":book}
    return render(request,"Book/book_detail.html",context)

def update(request):
    pass

def delete(request):
    pass

def index(request):
    return render(request,"Book/index.html",{})