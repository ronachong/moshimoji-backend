import graphene

from graphene_django.filter.fields import DjangoFilterConnectionField

from config.logger_import import logger
from project.gql_platform.graphene.user_sessions.objects import UserNode, UserStatusNode
from project.gql_platform.models import UserStatus


''' Query type definition for GraphQL server '''
class Query(graphene.ObjectType):
    # field definitions
    current_user = graphene.Field(UserNode)
    user = graphene.relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)
    all_user_statuses = DjangoFilterConnectionField(UserStatusNode, order_by_arg=graphene.String())

    # field resolvers
    # field resolvers for 'connection', Relay node fields skipped since it seems
    # DjangoFilterConnectionField and relay replace functionality

    def resolve_current_user(self, info):
        if not info.context.user.is_authenticated():
            return None
        return info.context.user

    def resolve_all_user_statuses(self, info, **args):
        logger.info("MM: resolve_all_user_statuses running")
        logger.info("MM: len of resolve_all_user_statuses return: %i" %
        len(UserStatus.objects.order_by("-creation_date")))
        return UserStatus.objects.order_by("-creation_date")
