from django.contrib import admin

# Register models here.
from project.gql_platform.models.content.social import UserStatus

admin.site.register(UserStatus)
