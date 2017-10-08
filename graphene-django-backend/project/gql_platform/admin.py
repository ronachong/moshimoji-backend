from django.contrib import admin

# Register your models here.
from .models import UserStatus, MangaSeries, Genre, Author

admin.site.register(UserStatus)
admin.site.register(MangaSeries)
admin.site.register(Genre)
admin.site.register(Author)
