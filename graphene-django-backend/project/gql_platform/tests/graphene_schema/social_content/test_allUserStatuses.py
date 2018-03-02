import pytest

from project.gql_platform.models.content.social.status_feed import UserStatus
from project.gql_platform.tests.graphene_schema.base import ConnectionFilterFieldTestSuite

pytestmark = pytest.mark.django_db

class TestAllUserStatuses(ConnectionFilterFieldTestSuite):
    @pytest.fixture
    def field(self):
        return 'allUserStatuses'

    @pytest.fixture
    def model(self):
        return UserStatus
