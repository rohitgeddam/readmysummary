from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Book, Chapter

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = "home.html"