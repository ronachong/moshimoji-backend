import logging
import pytest

from mixer.backend.django import mixer

from django.contrib.auth.models import User
from project.gql_platform.models import UserStatus

# following https://github.com/mbrochh/django-graphql-apollo-react-demo#add-jwt
# pytestmark makes writing to db possible in test
pytestmark = pytest.mark.django_db
logger = logging.getLogger('django')

def test_user_status_model():
    '''Test successful creation of UserStatus instance and storage in DB.'''
    inst = mixer.blend('gql_platform.UserStatus')
    assert inst.pk > 0

class TestOrderByFunctionality(object):
    @pytest.mark.django_db
    def test_with_all_user_statuses(self):
        user = mixer.blend(User)
        mixer.blend(UserStatus, user=user)
        mixer.blend(UserStatus, user=user)
        mixer.blend(UserStatus, user=user)
        mixer.blend(UserStatus, user=user)
        #UserStatus(text='status 1')
        order_1 = UserStatus.objects.all().order_by('creation_date')
        #logger.info("TMODELS: order 1\n{}".format(order_1))
        print("TMODELS: order 1\n{}".format(order_1[0].creation_date))
        order_2 = UserStatus.objects.all().order_by('-creation_date')
        #logger.info("TMODELS: order 2\n{}".format(order_2[3].creation_date))
        print("TMODELS: order 2\n{}".format(order_2[3].creation_date))
        assert order_1[0].creation_date == order_2[3].creation_date
