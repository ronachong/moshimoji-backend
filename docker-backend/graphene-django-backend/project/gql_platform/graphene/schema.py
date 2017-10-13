import django_filters
import graphene
import json

from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField

from project.gql_platform.models import UserStatus, Genre, Author, MangaSeries


# for clarification on the boilerplate in this file, first read graphene docs.
# then read at docs.graphene-python.org
# you could also read about models under django

''' Object type definitions for GraphQL server '''
# do I want everything to be a node, or just certain types?

class UserStatusNode(DjangoObjectType):
    class Meta:
        model = UserStatus
        filter_fields = ['user', 'text', 'creation_date']
        interfaces = (graphene.relay.Node, )

class UserStatusConnection(graphene.relay.Connection):
    class Meta:
        node = UserStatusNode

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['id']
        interfaces = (graphene.relay.Node, )

# seems like this version of classes to get User
# class UserStatusConnection(graphene.relay.Connection)
#     class Meta:
#         node = UserStatusNode
#
# class User(DjangoObjectType):
#     class Meta:
#         model = UserStatus
#     statuses = graphene.relay.ConnectionField(UserStatusConnection)
#
#     def resolve_ships(self, info):
#         return graphene.relay.ConnectionField.resolve_connection(
#             UserStatusConnection,
#             args,
#             ???
#         )

# not using custom filter set atm
# class UserStatusFilter(django_filters.FilterSet):
#     # Do case-insensitive partial lookups on 'text'
#     text = django_filters.CharFilter(lookup_expr=['icontains'])
#
#     class Meta:
#         model = UserStatus
#         fields = ['user', 'text', 'creation_date']

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
    user = graphene.relay.Node.Field(UserNode)
    genre = graphene.relay.Node.Field(GenreNode)
    author = graphene.relay.Node.Field(AuthorNode)
    manga_series = graphene.relay.Node.Field(MangaSeriesNode)

    # even though doc says to explicitly declare connections, it seems like I
    # don't need to do this to have a userStatusConnection/access userStatusSet?
    # user_status_connections = graphene.relay.ConnectionField(UserStatusConnection)

    all_users = DjangoFilterConnectionField(UserNode)
    # all_user_statuses = DjangoFilterConnectionField(UserStatusNode, filterset_class=UserStatusFilter)
    all_user_statuses = DjangoFilterConnectionField(UserStatusNode)
    all_genres = DjangoFilterConnectionField(GenreNode)
    all_authors = DjangoFilterConnectionField(AuthorNode)
    all_manga_series = DjangoFilterConnectionField(MangaSeriesNode)

    # field resolvers for 'connection', Relay node fields skipped since
    # DjangoFilterConnectionField and relay replace functionality, it seems?

    # def resolve_user_statuses(self, info):
    #     return graphene.relay.ConnectionField.resolve_connection(
    #         UserStatusConnection,
    #         args,
    #         UserStatus.objects.filter(user=User.objects.all()[0])
    #     )

    # if I add resolvers for relay node fields, they seem ineffectual. how am I
    # supposed to add handlers for custom args?



''' Mutation field definitions for GraphQL server '''
class CreateUserStatusMutation(graphene.Mutation):
    class Arguments:
        text = graphene.String()

    req_status = graphene.Int()
    form_errors = graphene.String()
    user_status = graphene.Field(UserStatusNode)

    @staticmethod
    # def mutate(root, args, context, info, text=None):
    def mutate(root, info, text=None):
        if not info.context['user'].is_authenticated():
            return CreateUserStatusMutation(req_status=403)

        if not isinstance(text, str) or not text:
            return CreateUserStatusMutation(
                req_status=400,
                form_errors=json.dumps(
                    {'status': ['Please enter text for the status.'] }
                )
            )

        obj = UserStatus.objects.create(
            user=info.context['user'],
            text=text,
        )

        # instead of user_status=obj, shouldn't it be user_status=node..?
        return CreateUserStatusMutation(
            req_status=200,
            form_errors=None,
            user_status=obj
        )

''' Mutation type definition for GraphQL server '''
class Mutation(graphene.ObjectType):
    create_user_status = CreateUserStatusMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
