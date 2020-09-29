from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse 
# Create your models here.
class Book(models.Model):

    GENRE_CHOICE = (
        ('self help', 'self help'),
        ('crime', 'crime'),
        ('fiction', 'fiction'),
        ('non fiction', 'non fiction'),
        ('other', 'other'),
    )

    LABEL_CHOICE = (
        ('want to read', 'want to read'),
        ('currently reading', 'currently reading'),
        ('completed', 'completed'),
        ('pause', 'pause')
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.CharField(max_length=255)
    description = RichTextField(default="")
    total_chapters = models.PositiveIntegerField(default=0)
    chapters_read = models.PositiveIntegerField(default=0, null=True,blank=True)
    started_on = models.DateField(null=True,blank=True)
    completed_on = models.DateField(null=True,blank=True)
    my_review = RichTextField(null=True,blank=True)
    genre = models.CharField(max_length=255, choices=GENRE_CHOICE, default='other')
    cover_image = models.ImageField(upload_to="covers/", null=True,blank=True)
    status = models.CharField(max_length=255, choices=LABEL_CHOICE, default='currently reading')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.slug),])

class Chapter(models.Model):
    book = models.ForeignKey(Book, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ch_no = models.PositiveIntegerField(default=0)
    summary = RichTextField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chapter_detail', args=[str(self.book.slug), str(self.slug),])