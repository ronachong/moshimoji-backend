import graphene

from graphene_django.types import DjangoObjectType

from project.example_app.models import Genre, Author, MangaSeries

# for clarification on the boilerplate in this file, first read graphene docs.
# then read at docs.graphene-python.org
# you could also read about models under django

''' Object type definitions for GraphQL server '''
class GenreType(DjangoObjectType):
    class Meta:
        model = Genre

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

class MangaSeriesType(DjangoObjectType):
    class Meta:
        model = MangaSeries


''' Query type definition(s) for GraphQL server, with resolver defs '''
class Query(graphene.ObjectType):
    all_genres = graphene.List(GenreType)
    all_authors = graphene.List(AuthorType)

    def resolve_all_genres(self, info, **kwargs):
        return Genre.objects.all()

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

schema = graphene.Schema(query=Query)
