import graphene

from graphene_django.types import DjangoObjectType

from project import logger
from project.gql_platform.graphene_schema import social_content, user_sessions
from project.gql_platform.graphene_schema.serialized_content import comic


''' Query type definition for GraphQL server '''
class Query(
    user_sessions.Query,
    social_content.Query,
    comic.Query,
    graphene.ObjectType):
    pass

''' Mutation type definition for GraphQL server '''
class Mutation(social_content.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
