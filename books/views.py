from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Chapter

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = "home.html"

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "book_detail.html"
    
class ChapterDetailView(DetailView):
    model = Chapter
    context_object_name = 'chapter'
    template_name = "chapter_detail.html"
    