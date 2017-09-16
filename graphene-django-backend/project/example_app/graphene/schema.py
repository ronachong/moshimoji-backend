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
        interfaces = (graphene.Node, )

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ['first_name', 'last_name']
        interfaces = (graphene.Node, )

class MangaSeriesType(DjangoObjectType):
    class Meta:
        model = MangaSeries
        filter_fields = ['title', 'author', 'genre']
        interfaces = (graphene.Node, )


''' Query type definition for GraphQL server '''
class Query(graphene.ObjectType):
    # field definitions
    genre = graphene.Field(GenreNode,
        id=graphene.Int(),
        name=graphene.String()
    )
    author = graphene.Field(AuthorType,
        id=graphene.Int(),
        first_name=graphene.String(),
        last_name=graphene.String()
    )
    manga_series = graphene.Field(MangaSeriesType,
        id=graphene.Int(),
        title=graphene.String(),
    )

    all_genres = DjangoFilterConnectionField(GenreNode)
    all_authors = DjangoFilterConnectionField(AuthorType)
    all_manga_series = DjangoFilterConnectionField(MangaSeriesType)

    # field resolvers (resolvers for 'connection' fields skipped since
    # DjangoFilterConnectionField supplies functionality)
    def resolve_genre(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id: # should not be None
            return Genre.objects.get(pk=id)
        if name:
            return Genre.objects.get(name=name)
        return None

    def resolve_author(self, info, **kwargs):
        """TBI"""
        pass

    def resolve_manga_series(self, info, **kwargs):
        """TBI"""
        pass

schema = graphene.Schema(query=Query)
