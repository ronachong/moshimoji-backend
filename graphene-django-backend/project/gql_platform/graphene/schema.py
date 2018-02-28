import graphene

from graphene_django.types import DjangoObjectType

from project import logger
from project.gql_platform.graphene import social_content, user_sessions


''' Query type definition for GraphQL server '''
class Query(
    user_sessions.Query,
    social_content.Query,
    graphene.ObjectType):
    pass

''' Mutation type definition for GraphQL server '''
class Mutation(social_content.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
