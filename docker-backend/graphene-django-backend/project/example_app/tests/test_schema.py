import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
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

    assert len(executed['data']['allUserStatuses']['edges']) == 3, (
        'Should return count of all messages in DB')

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

class TestCreateUserStatusMutationClass(object):
    @pytest.fixture
    def user_status_mut():
        return schema.CreateUserStatusMutation()

    @pytest.fixture
    def user():
        return mixer.blend('auth.User')

    # @pytest.fixture
    # def good_data_input():
    #     return {'status': 'Test submission'}

    # @pytest.fixture
    # def get_req_to_root():
    #     return RequestFactory().get('/')

    def test_mut_res_when_user_not_logged_in(user_status_mut):
        data = {'status': 'Test submission'}
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        res = user_status_mut.mutate(None, data, req, None)
        assert res.status == 403, 'Should return 403 if user is not logged in'

    def test_mut_res_when_form_improper(user_status_mut, user):
        data = {}
        req = RequestFactory().get('/')
        req.user = user
        res = mut.mutate(None, data, req, None)
        assert res.status == 400, 'Should return 400 if there are form errors'
        assert 'message' in res.formErrors, (
            'Should have form error for message field')

    def test_mut_res_when_form_proper_and_user_logged_in(user_status_mut, user):
        data = {'status': 'Test submission'}
        req.user = user
        res = mut.mutate(None, data, req, None)
        assert res.status == 200, (
            'Should return 200 if there are no form errors and user logged in')
        assert res.message.pk == 1, 'Should create new message'
