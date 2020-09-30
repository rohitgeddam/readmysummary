from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Chapter

# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["currently_reading_list"] = Book.objects.filter(status="currently reading")
        data["already_read_list"] = Book.objects.filter(status="completed")
        return data
class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "book_detail.html"
    
class ChapterDetailView(DetailView):
    model = Chapter
    context_object_name = 'chapter'
    template_name = "chapter_detail.html"

def WishListView(request):
    book_list = Book.objects.filter(status="want to read")

    context = {"book_list": book_list}
    
    return render(request, 'wishlist_list.html', context)