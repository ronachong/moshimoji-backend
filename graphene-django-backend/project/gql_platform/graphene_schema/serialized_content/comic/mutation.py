# import graphene
#
# from project.gql_platform.models.content.serialization.comic import Genre
# from project.gql_platform.graphene_schema.serialized_content.comic.objects import Genre
#
# # NOTE: eventually this might be used somewhere (e.g. if site staff needed to
# # be able to add genres for series to the site. but for now I'll probably just
# # populate the genre options via a script)
#
# ''' Mutation field definitions for GraphQL server '''
# class CreateGenreMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String()
#
#     req_status = graphene.Int()
#     form_errors = graphene.String()
#     genre = graphene.Field(Genre)
#
#     @staticmethod
#     def mutate(root, info, name=None):
#         if not info.context.user.is_authenticated():
#             return CreateGenreMutation(
#                 req_status=403,
#                 genre=None,
#                 form_errors=None
#             )
#
#         if not isinstance(name, str) or not name:
#             return CreateGenreMutation(
#                 req_status=400,
#                 genre=None,
#                 form_errors=json.dumps(
#                     {'status': ['Please enter a name for the genre to be created.'] }
#                 )
#             )
#
#         obj = Genre.objects.create(
#             name=name,
#         )
#
#         return CreateGenreMutation(
#             req_status=200,
#             form_errors=None,
#             genre=obj
#         )
#
# ''' Mutation type definition for GraphQL server '''
# class Mutation(graphene.ObjectType):
#     create_genre = CreateGenreMutation.Field()
