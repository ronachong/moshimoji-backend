import pytest
from mixer.backend.django import mixer

from ..graphene.schema import schema
from graphene import Schema
from graphene.test import Client

pytestmark = pytest.mark.django_db

def test_user_status_type():
    '''Test that GraphQL type for UserStatus model exists and can be used.'''
    instance = schema.UserStatusNode()
    assert instance

def test_all_user_statuses():
    '''Test that query for allUserStatuses field returns resp of expected len.'''
    graphene_client = Client(schema)
    executed = graphene_client.execute('''{
        allUserStatuses {
            edges {
                node {
                    id,
                    text
                }
            }
        }
    }''')
    assert len(executed['data']['allUserStatuses']['edges']) == 0

    mixer.blend('example_app.UserStatus')
    mixer.blend('example_app.UserStatus')
    mixer.blend('example_app.UserStatus')

    executed = graphene_client.execute('''{
        allUserStatuses {
            edges {
                node {
                    id,
                    text
                }
            }
        }
    }''')

    # debug prints
    print (schema.__class__.__name__)
    print (isinstance(schema, Schema))
    print(executed)

    assert len(executed['data']['allUserStatuses']['edges']) == 3, 'Should return count of all messages in DB'

    # In mbrocch's tests, he tests the resolver for all user_statuses.
    # Since I do not specify a resolver and do not know how the DjangoConnxnField
    # resolver gets called in practice, I've skip this test for now.
    # q = schema.Query()
    # res = q.all_user_statuses
    # print(
    #     dir(res),
    #     res.default_value,
    #     res.connection_resolver(),
    #     )
    #assert res.count() == 2, 'Should return count of all messages in DB'
