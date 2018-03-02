import graphene
from graphene_django.types import DjangoObjectType

from project.gql_platform.models.content.serialization import comic

from project import logger

''' Object type definitions for GraphQL server '''
# TODO: determine if I want everything to be a node, or just certain object types
class GenreNode(DjangoObjectType):
    class Meta:
        model = comic.Genre
        filter_fields = ['name']
        interfaces = (graphene.relay.Node, )

# class GenreConnection(graphene.relay.Connection):
#     class Meta:
#         node = GenreNode
