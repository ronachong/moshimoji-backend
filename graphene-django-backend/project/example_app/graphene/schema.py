import graphene

from graphene_django.types import DjangoObjectType
# from graphene_django.filter import

from project.example_app.models import Genre, Author, MangaSeries

# for clarification on the boilerplate in this file, first read graphene docs.
# then read at docs.graphene-python.org
# you could also read about models under django

''' Object type definitions for GraphQL server '''
class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        interfaces = (graphene.Node, )

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        interfaces = (graphene.Node, )

class MangaSeriesType(DjangoObjectType):
    class Meta:
        model = MangaSeries
        interfaces = (graphene.Node, )


''' Query type definition for GraphQL server, with resolver defs for fields '''
class Query(graphene.ObjectType):
    genre = graphene.Field(GenreType,
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

    all_genres = graphene.List(GenreType)
    all_authors = graphene.List(AuthorType)
    all_manga_series = graphene.List(MangaSeriesType)

    def resolve_genre(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id: # should not be None
            return Genre.objects.get(pk=id)
        if name:
            return Genre.objects.get(name=name)
        return None

    def resolve_all_genres(self, info, **kwargs):
        return Genre.objects.all()

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_all_manga_series(self, info, **kwargs):
        return MangaSeries.objects.all()

schema = graphene.Schema(query=Query)
