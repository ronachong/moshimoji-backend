import graphene
from graphene_django.types import DjangoObjectType

from misago.users.models.user import User as MisagoUser

from config.logger_import import logger

''' Object type definitions for GraphQL server '''

class UserNode(DjangoObjectType):
    class Meta:
        model = MisagoUser
        filter_fields = ['id']
        interfaces = (graphene.relay.Node, )
