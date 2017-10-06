import pytest
from mixer.backend.django import mixer

from ..graphene import schema

pytestmark = pytest.mark.django_db

def test_status_type():
    '''Test that GraphQL type for Status model exists and can be used.'''
    instance = schema.StatusType()
    assert instance

def test_resolve_all_statuses():
    mixer.blend('example_app.Status')
    mixer.blend('example_app.Status')
    q = schema.Query()
    res = q.resolve_all_statuses(None, None, None)
    assert res.count() == 2, 'Should return count of all messages in DB'
