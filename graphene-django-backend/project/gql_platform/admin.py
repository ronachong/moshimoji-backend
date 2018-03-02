from django.contrib import admin

# Register models here.
from project.gql_platform.models.content.social import UserStatus
from project.gql_platform.models.content.serialization.comic import Genre

admin.site.register(UserStatus)
admin.site.register(Genre)
