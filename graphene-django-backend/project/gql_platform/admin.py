from django.contrib import admin

# Register models here.
from project.gql_platform.models.content.social import UserStatus
from project.gql_platform.models.content.serialization.comic import Genre, Serialization

gql_models = [
    UserStatus,
    Genre,
    Serialization
]

for model in gql_models:
    admin.site.register(model)
