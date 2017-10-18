import pytest
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from graphene.test import Client
from graphene import Schema
from graphql.execution.base import ResolveInfo
from mixer.backend.django import mixer

from ..graphene.schema import schema

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

    mixer.blend('gql_platform.UserStatus')
    mixer.blend('gql_platform.UserStatus')
    mixer.blend('gql_platform.UserStatus')

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
    def CreateUserStatusMutation_inst(self):
            return schema.CreateUserStatusMutation()

    @pytest.fixture
    def user(self):
        return mixer.blend('auth.User')

    @pytest.fixture
    def anon(self):
        return AnonymousUser()

    @pytest.fixture
    def proper_input(self):
        return {'text': 'Test submission'}

    @pytest.fixture
    def dummy_info(self):
        return ResolveInfo(
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        )

    def test_mut_res_when_user_not_logged_in(
        self, CreateUserStatusMutation_inst, proper_input, anon, dummy_info):
        dummy_info.context = {'user': anon}
        res = CreateUserStatusMutation_inst.mutate(None, dummy_info, **proper_input)
        assert res.req_status == 403, 'Should return 403 if user is not logged in'

    def test_mut_res_when_form_improper(self, CreateUserStatusMutation_inst, user, dummy_info):
        dummy_info.context = {'user': user}
        res = CreateUserStatusMutation_inst.mutate(None, dummy_info, **{})
        assert res.req_status == 400, 'Should return 400 if there are form errors'
        assert 'text' in res.form_errors, (
            'Should have form error for user status field')

    def test_mut_res_when_form_proper_and_user_logged_in(
        self, CreateUserStatusMutation_inst, user, proper_input, dummy_info):
        dummy_info.context = {'user': user}
        res = CreateUserStatusMutation_inst.mutate(None, dummy_info, **proper_input)
        assert res.req_status == 200, (
            'Should return 200 if there are no form errors and user logged in')
        assert res.user_status.pk == 1, 'Should create new message'

    def test_mut_res_when_form_proper_and_user_logged_in_2(self, user):
        '''Note that this test actually checks that resolver works with graphene.
        (Other unit tests only check that mutation resolver behaves as intended)
        '''
        graphene_client = Client(
            schema,
        )
        executed = graphene_client.execute(
            '''mutation {
                createUserStatus(text: "Test") {
                    userStatus {
                        id,
                        text
                    }
                    formErrors,
                    reqStatus
                }
            }''',
            context_value={'user': user},
        )
        print(executed)

        assert executed['data']['createUserStatus']['userStatus']['text'] == "Test", (
            'Should be status text submitted in mutation')
