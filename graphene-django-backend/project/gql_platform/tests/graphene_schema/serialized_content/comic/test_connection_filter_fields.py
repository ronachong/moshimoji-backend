import pytest

from project.gql_platform.models.content.serialization.comic import Genre, Serialization
from project.gql_platform.tests.graphene_schema.base import ConnectionFilterFieldTestSuite

pytestmark = pytest.mark.django_db

class TestAllGenres(ConnectionFilterFieldTestSuite):
    @pytest.fixture
    def field(self):
        return 'allGenres'

    @pytest.fixture
    def model(self):
        return Genre

    @pytest.fixture
    def sort_field(self):
        return 'name'

    @pytest.fixture
    def sort_prototype(self):
        return [
            { "name": 'alpha' },
            { "name": 'beta' },
            { "name": 'gamma' },
        ]

class TestAllSeries(ConnectionFilterFieldTestSuite):
    @pytest.fixture
    def field(self):
        return 'allSeries'

    @pytest.fixture
    def model(self):
        return Serialization

    @pytest.fixture
    def sort_field(self):
        return 'title'

    @pytest.fixture
    def sort_prototype(self):
        return [
            { "title": 'alpha' },
            { "title": 'beta' },
            { "title": 'gamma' },
        ]
