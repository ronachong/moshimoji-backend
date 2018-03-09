import graphene

from graphene_django.filter.fields import DjangoFilterConnectionField

from project import logger
from project.gql_platform.graphene_schema.graphene_django_hacks import CustomDjangoFilterConnectionField
from project.gql_platform.graphene_schema.serialized_content.comic.objects import GenreNode, SerializationNode
from project.gql_platform.models.content.serialization.comic import Genre



''' Query type definition for GraphQL server '''
class Query(graphene.ObjectType):
    # field definitions
    all_genres = DjangoFilterConnectionField(
        GenreNode,
        # order_by_arg=graphene.String()
    )
    all_series = CustomDjangoFilterConnectionField(
        SerializationNode,
        # order_by_arg=graphene.string()
    )

    # field resolvers
    # field resolvers for
    #   - Relay connection fields (e.g. UserStatusConnection)
    #   - Relay node fields (e.g. UserStatusNode)
    # are skipped since it seems DjangoFilterConnectionField and relay implement
    # these resolvers for us

    def resolve_all_genres(self, info, **args):
        return Genre.objects.order_by("name")

    def resolve_all_series(self, info, **args):
        return Series.objects.order_by("title")
        # return Series.objects.all()
