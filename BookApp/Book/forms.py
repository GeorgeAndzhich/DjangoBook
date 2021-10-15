from django import forms
from .models import Book
class BookForm (ModelForm):
    class Meta:
        model = Book
        fields = '__all__'