import graphene

from graphene_django.types import DjangoObjectType

from config.logger_import import logger
from project.gql_platform.graphene import user_sessions


''' Query type definition for GraphQL server '''
class Query(user_sessions.Query, graphene.ObjectType):
    pass

''' Mutation type definition for GraphQL server '''
class Mutation(user_sessions.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
