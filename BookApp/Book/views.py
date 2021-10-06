from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,ListView
from .models import Book
from django.urls import reverse_lazy

# Create your views here.
class CreateBookView(CreateView):
    model = Book
    pass


class BookListView(ListView):
    model = Book
    pass