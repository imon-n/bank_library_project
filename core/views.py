from django.shortcuts import render
from django.views.generic import TemplateView
from book.models import Book_Model
from category_book.models import CategoryModel

def home(request, category_slug = None):
    data = Book_Model.objects.all()
    categorys = CategoryModel.objects.all()
    if category_slug is not None:
        category_name = CategoryModel.objects.get(slug = category_slug)
        data = Book_Model.objects.filter(category_name  = category_name)
    return render(request, 'home.html', {'data' : data, 'categorys':categorys})

def front(request):
    return render(request, 'front.html')

class HomeView(TemplateView):
    template_name = 'index.html'
