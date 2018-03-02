import pytest

from project.gql_platform.models.content.serialization.comic import Genre
from project.gql_platform.tests.graphene_schema.base import ConnectionFilterFieldTestSuite

pytestmark = pytest.mark.django_db

class TestAllGenres(ConnectionFilterFieldTestSuite):
    @pytest.fixture
    def field(self):
        return 'allGenres'

    @pytest.fixture
    def model(self):
        return Genre
