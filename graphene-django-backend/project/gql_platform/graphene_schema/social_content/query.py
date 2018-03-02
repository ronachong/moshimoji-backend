import graphene

from graphene_django.filter.fields import DjangoFilterConnectionField

from project import logger
from project.gql_platform.graphene_schema.social_content.objects import UserStatusNode
from project.gql_platform.models.content.social import UserStatus


''' Query type definition for GraphQL server '''
class Query(graphene.ObjectType):
    # field definitions
    all_user_statuses = DjangoFilterConnectionField(UserStatusNode, order_by_arg=graphene.String())

    # field resolvers
    # field resolvers for 'connection', Relay node fields skipped since it seems
    # DjangoFilterConnectionField and relay replace functionality

    def resolve_all_user_statuses(self, info, **args):
        logger.info("MM: resolve_all_user_statuses running")
        logger.info("MM: len of resolve_all_user_statuses return: %i" %
        len(UserStatus.objects.order_by("-creation_date")))
        return UserStatus.objects.order_by("-creation_date")
