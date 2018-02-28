import graphene

from project.gql_platform.models import UserStatus
from project.gql_platform.graphene.user_sessions.objects import UserStatusNode

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
