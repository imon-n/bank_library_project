from django import forms
from .models import Book_Model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book_Model
        fields = '__all__'
