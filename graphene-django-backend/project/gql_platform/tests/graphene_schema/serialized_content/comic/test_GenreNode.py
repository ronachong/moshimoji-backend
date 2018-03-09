import pytest

from project.gql_platform.graphene_schema.schema import schema
from project.gql_platform.tests.graphene_schema.base import NodeTestSuite

class TestGenreNode(NodeTestSuite):
    @pytest.fixture
    def node_class(self):
        return(schema.GenreNode)
