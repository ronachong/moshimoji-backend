import pytest
from mixer.backend.django import mixer

# following https://github.com/mbrochh/django-graphql-apollo-react-demo#add-jwt
# pytestmark makes writing to db possible in test
pytestmark = pytest.mark.django_db

def test_user_status_model():
    '''Test successful creation of UserStatus instance and storage in DB.'''
    inst = mixer.blend('example_app.UserStatus')
    assert inst.pk > 0
