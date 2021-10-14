from django import forms
from .models import Book
class BookForm (ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = ["Author",
         "Name",
         "Comment"
            ]