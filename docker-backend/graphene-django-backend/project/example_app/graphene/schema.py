import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField

from project.example_app.models import Genre, Author, MangaSeries

# for clarification on the boilerplate in this file, first read graphene docs.
# then read at docs.graphene-python.org
# you could also read about models under django

''' Object type definitions for GraphQL server '''
class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = {
            'name': ['icontains', 'exact'],
        }
        interfaces = (graphene.relay.Node, )

class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ['first_name', 'last_name']
        interfaces = (graphene.relay.Node, )

class MangaSeriesNode(DjangoObjectType):
    class Meta:
        model = MangaSeries
        filter_fields = ['title', 'author', 'genre']
        interfaces = (graphene.relay.Node, )


''' Query type definition for GraphQL server '''
class Query(graphene.ObjectType):
    # field definitions
    genre = graphene.relay.Node.Field(GenreNode)
    author = graphene.relay.Node.Field(AuthorNode)
    manga_series = graphene.relay.Node.Field(MangaSeriesNode)

    all_genres = DjangoFilterConnectionField(GenreNode)
    all_authors = DjangoFilterConnectionField(AuthorNode)
    all_manga_series = DjangoFilterConnectionField(MangaSeriesNode)

    # field resolvers for 'connection', Relay node fields skipped since
    # DjangoFilterConnectionField and relay replace functionality

    # if I add resolvers for relay node fields, they seem ineffectual. how am I
    # supposed to add handlers for custom args?

schema = graphene.Schema(query=Query)
