import graphene
from graphene_django.types import DjangoObjectType

from project.gql_platform.models.content.serialization import comic

from project import logger

''' Object type definitions for GraphQL server '''
# TODO: determine if I want everything to be a node, or just certain object types
class GenreNode(DjangoObjectType):
    class Meta:
        model = comic.Genre
        # TODO: add icontains sorting for name and test
        filter_fields = { 'name': ['icontains'] }
        interfaces = (graphene.relay.Node, )

# class GenreConnection(graphene.relay.Connection):
#     class Meta:
#         node = GenreNode

class SerializationNode(DjangoObjectType):
    class Meta:
        model = comic.Serialization
        filter_fields = {
            'title': ['icontains']
            #'author',
            # 'genres' - think I can set up a resolver to return series list by genre
        }

# class SerializationConnection(graphene.relay.Connection):
#     class Meta:
#         node = SerializationNode
