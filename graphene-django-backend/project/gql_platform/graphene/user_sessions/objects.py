import graphene
from graphene_django.types import DjangoObjectType

from misago.users.models.user import User as MisagoUser
from project.gql_platform.models import UserStatus

from config.logger_import import logger

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

class UserNode(DjangoObjectType):
    class Meta:
        model = MisagoUser
        filter_fields = ['id']
        interfaces = (graphene.relay.Node, )
