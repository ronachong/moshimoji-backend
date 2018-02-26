import django_filters
import graphene
import json

from django.contrib.auth.models import User
from misago.users.models.user import User as MisagoUser
from config.settings import base as settings
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField

from config.logger_import import logger
from project.gql_platform.models import UserStatus, Genre, Author, MangaSeries


# for clarification on the boilerplate in this file, first read graphene docs.
# then read at docs.graphene-python.org
# you could also read about models under django

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

class GenreNode(DjangoObjectType):
    class Meta:
        model = Genre
        filter_fields = {
            'name': ['icontains', 'exact'],
        }
        interfaces = (graphene.relay.Node, )

class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ['first_name', 'last_name']
        interfaces = (graphene.relay.Node, )

class MangaSeriesNode(DjangoObjectType):
    class Meta:
        model = MangaSeries
        filter_fields = ['title', 'author', 'genre']
        interfaces = (graphene.relay.Node, )

''' Query type definition for GraphQL server '''
class Query(graphene.ObjectType):
    # field definitions
    current_user = graphene.Field(UserNode)

    user = graphene.relay.Node.Field(UserNode)
    genre = graphene.relay.Node.Field(GenreNode)
    author = graphene.relay.Node.Field(AuthorNode)
    manga_series = graphene.relay.Node.Field(MangaSeriesNode)

    all_users = DjangoFilterConnectionField(UserNode)
    #all_user_statuses = DjangoFilterConnectionField(UserStatusNode)
    # test_arg = graphene.String().Argument(name='test_arg')
    # test_arg = graphene.String(description="test", required=False).Argument()
    # test_arg = graphene.String()
    # all_user_statuses = DjangoFilterConnectionField(UserStatusNode, test_arg)
    all_user_statuses = DjangoFilterConnectionField(UserStatusNode, order_by_arg=graphene.String())
    all_genres = DjangoFilterConnectionField(GenreNode)
    all_authors = DjangoFilterConnectionField(AuthorNode)
    all_manga_series = DjangoFilterConnectionField(MangaSeriesNode)

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

    # def resolve_user_statuses(self, info):
    #     return graphene.relay.ConnectionField.resolve_connection(
    #         UserStatusConnection,
    #         args,
    #         UserStatus.objects.filter(user=User.objects.all()[0])
    #     )

''' Mutation field definitions for GraphQL server '''
class CreateUserStatusMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String()

    req_status = graphene.Int()
    form_errors = graphene.String()
    user_status = graphene.Field(UserStatusNode)

    @staticmethod
    def mutate(root, info, text=None):
        if not info.context.user.is_authenticated():
            return CreateUserStatusMutation(
                req_status=403,
                user_status=None,
                form_errors=None
            )

        if not isinstance(text, str) or not text:
            return CreateUserStatusMutation(
                req_status=400,
                user_status=None,
                form_errors=json.dumps(
                    {'status': ['Please enter text for the status.'] }
                )
            )

        obj = UserStatus.objects.create(
            user=info.context.user,
            text=text,
        )

        return CreateUserStatusMutation(
            req_status=200,
            form_errors=None,
            user_status=obj
        )

''' Mutation type definition for GraphQL server '''
class Mutation(graphene.ObjectType):
    create_user_status = CreateUserStatusMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
