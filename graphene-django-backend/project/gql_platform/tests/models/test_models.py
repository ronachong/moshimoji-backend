import logging
import pytest

from mixer.backend.django import mixer

from misago.users.models.user import User as MisagoUser
from project.gql_platform.models.content.social import UserStatus
from project.gql_platform.models.content.serialization import comic

# following https://github.com/mbrochh/django-graphql-apollo-react-demo#add-jwt
# pytestmark makes writing to db possible in test
pytestmark = pytest.mark.django_db
logger = logging.getLogger('django')

def test_user_model():
    '''Test successful creation of User instance and storage in DB.'''
    inst = mixer.blend(MisagoUser)
    assert inst.pk > 0

def test_user_status_model():
    '''Test successful creation of UserStatus instance and storage in DB.'''
    test_username = 'arromatic'
    inst = mixer.blend(UserStatus, user__username=test_username)
    assert inst.pk > 0
    assert inst.user.username == test_username

def test_genre_model():
    '''Test successful creation of UserStatus instance and storage in DB.'''
    test_name = 'Drama'
    inst = mixer.blend(
        comic.Genre,
        name=test_name
    )
    assert inst.pk > 0
    assert inst.name == test_name
    assert str(inst) == test_name

class TestComicSerializationModel(object):
    def test_model(self):
        '''Test successful creation of Serialization instance and storage in DB.'''
        test_title = 'Ran to Hairo'
        # test_author =
        inst = mixer.blend(
            comic.Serialization,
            title=test_title,
        )
        assert inst.pk > 0
        assert inst.title == test_title
        # assert inst.author

    def test_multi_genre_addition(self):
        '''Test successful addition of genres to comic series.'''
        test_genre1 = mixer.blend(comic.Genre)
        test_genre2 = mixer.blend(comic.Genre)
        inst = mixer.blend(comic.Serialization)
        inst.genres.add(test_genre1)
        inst.genres.add(test_genre2)
        assert test_genre1 in inst.genres.all()
        assert test_genre2 in inst.genres.all()

# class TestOrderByFunctionality(object):
#     @pytest.mark.django_db
#     def test_with_all_user_statuses(self):
#         user = mixer.blend(User)
#         mixer.blend(UserStatus, user=user)
#         mixer.blend(UserStatus, user=user)
#         mixer.blend(UserStatus, user=user)
#         mixer.blend(UserStatus, user=user)
#         #UserStatus(text='status 1')
#         order_1 = UserStatus.objects.all().order_by('creation_date')
#         #logger.info("TMODELS: order 1\n{}".format(order_1))
#         print("TMODELS: order 1\n{}".format(order_1[0].creation_date))
#         order_2 = UserStatus.objects.all().order_by('-creation_date')
#         #logger.info("TMODELS: order 2\n{}".format(order_2[3].creation_date))
#         print("TMODELS: order 2\n{}".format(order_2[3].creation_date))
#         assert order_1[0].creation_date == order_2[3].creation_date
