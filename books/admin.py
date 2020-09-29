from django.contrib import admin
import nested_admin
from .models import Book, Chapter
# Register your models here.


class ChapterAdmin(nested_admin.NestedStackedInline):
    model = Chapter
    prepopulated_fields = {"slug": ("title",)}
    extra = 0


class BookAdmin(nested_admin.NestedModelAdmin):

    inlines = [ChapterAdmin]
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Book, BookAdmin)
