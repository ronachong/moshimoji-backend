import graphene

from graphene_django.filter.fields import DjangoFilterConnectionField

from project import logger
from project.gql_platform.graphene.user_sessions.objects import UserNode


''' Query type definition for GraphQL server '''
class Query(graphene.ObjectType):
    # field definitions
    current_user = graphene.Field(UserNode)
    user = graphene.relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    # field resolvers
    # field resolvers for 'connection', Relay node fields skipped since it seems
    # DjangoFilterConnectionField and relay replace functionality

    def resolve_current_user(self, info):
        if not info.context.user.is_authenticated():
            return None
        return info.context.user
