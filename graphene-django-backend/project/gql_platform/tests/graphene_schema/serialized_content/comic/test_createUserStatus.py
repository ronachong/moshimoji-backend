# import pytest
# from mixer.backend.django import mixer
#
# from graphene import Schema
# from graphene.test import Client
# from graphql.execution.base import ResolveInfo
# from django.contrib.auth.models import AnonymousUser
# from misago.users.models.user import User as MisagoUser
# from project.gql_platform.graphene_schema.schema import schema
#
#
# pytestmark = pytest.mark.django_db
#
#
# class DummyContext(object):
#     def __init__(self, user):
#         self.user = user
#
# # TODO: refactor this test case
# class TestCreateUserStatusMutationClass(object):
#     @pytest.fixture
#     def CreateUserStatusMutation_inst(self):
#             return schema.CreateUserStatusMutation()
#
#     @pytest.fixture
#     def user(self):
#         return mixer.blend(MisagoUser)
#
#     @pytest.fixture
#     def anon(self):
#         return AnonymousUser()
#
#     @pytest.fixture
#     def proper_input(self):
#         return {'text': 'Test submission'}
#
#     @pytest.fixture
#     def dummy_context(self):
#         return
#
#     @pytest.fixture
#     def dummy_info(self):
#         return ResolveInfo(
#             None,
#             None,
#             None,
#             None,
#             None,
#             None,
#             None,
#             None,
#             None,
#             None
#         )
#
#     def test_mut_res_when_user_not_logged_in(
#         self, CreateUserStatusMutation_inst, proper_input, anon, dummy_info):
#         dummy_info.context = DummyContext(anon)
#         res = CreateUserStatusMutation_inst.mutate(None, dummy_info, **proper_input)
#         assert res.req_status == 403, 'Should return 403 if user is not logged in'
#
#     def test_mut_res_when_form_improper(self, CreateUserStatusMutation_inst, user, dummy_info):
#         dummy_info.context = DummyContext(user)
#         res = CreateUserStatusMutation_inst.mutate(None, dummy_info, **{})
#         assert res.req_status == 400, 'Should return 400 if there are form errors'
#         assert 'text' in res.form_errors, (
#             'Should have form error for user status field')
#
#     def test_mut_res_when_form_proper_and_user_logged_in(
#         self, CreateUserStatusMutation_inst, user, proper_input, dummy_info):
#         dummy_info.context = DummyContext(user)
#         res = CreateUserStatusMutation_inst.mutate(None, dummy_info, **proper_input)
#         assert res.req_status == 200, (
#             'Should return 200 if there are no form errors and user logged in')
#         assert res.user_status.pk == 1, 'Should create new message'
#
#     def test_mut_res_when_form_proper_and_user_logged_in_2(self, user):
#         '''Note that this test actually checks that resolver works with graphene.
#         (Other unit tests only check that mutation resolver behaves as intended)
#         '''
#         graphene_client = Client(
#             schema,
#         )
#         executed = graphene_client.execute(
#             '''mutation {
#                 createUserStatus(text: "Test") {
#                     userStatus {
#                         id,
#                         text
#                     }
#                     formErrors,
#                     reqStatus
#                 }
#             }''',
#             context_value=DummyContext(user),
#         )
#
#         assert executed['data']['createUserStatus']['userStatus']['text'] == "Test", (
#             'Should be status text submitted in mutation')
