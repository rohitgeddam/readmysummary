from django.contrib import admin
from django.urls import path
from .views import BookListView, BookDetailView,ChapterDetailView


urlpatterns = [
    path('<slug:slug>', BookDetailView.as_view(), name="book_detail"),
    path('<slug:book_slug>/<slug:slug>', ChapterDetailView.as_view(), name="chapter_detail"),
    
    path('', BookListView.as_view(), name="book_list"),
]
