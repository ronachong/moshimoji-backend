from django.contrib import admin

# Register your models here.
from .models import Status, MangaSeries, Genre, Author

admin.site.register(Status)
admin.site.register(MangaSeries)
admin.site.register(Genre)
admin.site.register(Author)
