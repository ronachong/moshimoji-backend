from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class MangaSeries(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, related_name='manga_series')
    genre = models.ForeignKey(Genre, related_name='manga_series')

    def __str__(self):
        return self.title
