import logging
import pytest

from project.gql_platform.models.content.serialization.comic import Genre
from project.gql_platform.initial_data.init_genres import genre_list, generate_genres

# pytestmark makes writing to db possible in test
pytestmark = pytest.mark.django_db
logger = logging.getLogger('django')

class TestGenerateGenres(object):
    def test_correct_number_entries_generated(self):
        '''Test that generate_genres creates as many entries in db as in genre_list.'''
        assert len(genre_list) != 0
        assert Genre.objects.count() == 0
        generate_genres()
        assert Genre.objects.count() == len(genre_list)

    def test_no_dups_generated(self):
        '''Test that generate_genres does not create genre if genre by name already exists.'''
        generate_genres()
        ct1 = Genre.objects.count()
        generate_genres()
        ct2 = Genre.objects.count()
        assert ct1 == ct2
