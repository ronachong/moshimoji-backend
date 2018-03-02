import graphene
from graphene_django.types import DjangoObjectType

from project.gql_platform.models.content.social import UserStatus

from project import logger

''' Object type definitions for GraphQL server '''
# TODO: determine if I want everything to be a node, or just certain object types
class UserStatusNode(DjangoObjectType):
    class Meta:
        model = UserStatus
        filter_fields = ['user', 'text', 'creation_date']
        # filter_order_by = ('creation_date')
        interfaces = (graphene.relay.Node, )

class UserStatusConnection(graphene.relay.Connection):
    class Meta:
        node = UserStatusNode
