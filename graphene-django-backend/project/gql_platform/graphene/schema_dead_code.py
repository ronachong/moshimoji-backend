# This file is just for reference in case I need to try any of these patterns
# in the future

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

    # all_user_statuses = DjangoFilterConnectionField(UserStatusNode, filterset_class=UserStatusFilter)

# even though doc says to explicitly declare connections, it seems like I
# don't need to do this to have a userStatusConnection/access userStatusSet?
# https://github.com/graphql-python/graphene/blob/2.0/UPGRADE-v2.0.md#node-connections
# user_status_connections = graphene.relay.ConnectionField(UserStatusConnection)



    # def resolve_user_statuses(self, info):
    #     return graphene.relay.ConnectionField.resolve_connection(
    #         UserStatusConnection,
    #         args,
    #         UserStatus.objects.filter(user=User.objects.all()[0])
    #     )
