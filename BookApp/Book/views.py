from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy

# Create your views here.
def read(request):
    books = Book.objects.all()
    context = {"book":books}
    return render (request,"Book/book_list.html",context)

def create(request): 
    form = BookForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(read)
    else:
        context = {"form":form}
        return render(request,"Book/book_create.html",context)


def update(request):
    pass

def delete(request):
    pass

def index(request):
    return render(request,"Book/index.html",{})