from django.db import models

# Create your models here.
class UserStatus(models.Model):
    user = models.ForeignKey('auth.User')
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".join(first_name, last_name)


class MangaSeries(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, related_name='manga_series')
    genre = models.ForeignKey(Genre, related_name='manga_series')

    def __str__(self):
        return self.title
