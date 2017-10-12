import graphene
import json

from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField

from project.gql_platform.models import UserStatus, Genre, Author, MangaSeries

# for clarification on the boilerplate in this file, first read graphene docs.
# then read at docs.graphene-python.org
# you could also read about models under django

''' Object type definitions for GraphQL server '''
class UserStatusNode(DjangoObjectType):
    class Meta:
        model = UserStatus
        # do I need any filter fields?
        filter_fields = {
            'user': ['exact']
        }
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
    genre = graphene.relay.Node.Field(GenreNode)
    author = graphene.relay.Node.Field(AuthorNode)
    manga_series = graphene.relay.Node.Field(MangaSeriesNode)

    all_user_statuses = DjangoFilterConnectionField(UserStatusNode)
    all_genres = DjangoFilterConnectionField(GenreNode)
    all_authors = DjangoFilterConnectionField(AuthorNode)
    all_manga_series = DjangoFilterConnectionField(MangaSeriesNode)

    # field resolvers for 'connection', Relay node fields skipped since
    # DjangoFilterConnectionField and relay replace functionality

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
