from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from .models import Book
from django.urls import reverse_lazy

# Create your views here.
class CreateBookView(CreateView):
    model = Book
    template_name = 'Book/create.html'
    pass


class BookListView(ListView):
    model = Book
    template_name = 'Book/index.html'
    pass

class UpdateBookView(UpdateView):
    pass