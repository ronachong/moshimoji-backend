import json
import pytest

from graphene.test import Client
from mixer.backend.django import mixer

from project.gql_platform.graphene_schema.schema import schema


class NodeTestSuite(object):
    @pytest.fixture
    def node_class(self):
        '''This gets overwritten by inheriting class'''
        return None

    def test_node_type_exists(self, node_class):
        '''Test that node_class represents GraphQL type of Node interface with fields'''
        assert node_class
        assert node_class._meta.__module__ == 'graphene_django.types'
        assert str(node_class._meta.interfaces[0]) == 'Node'
        assert node_class._meta.fields

    def test_node_registered_to_schema(self, node_class):
        '''Test that GraphQL type of same name is registered to master schema.'''
        for schema_type in schema.introspect()["__schema"]["types"]:
            if schema_type["name"] == node_class._meta.name:
                present = True
                break

        assert present

    # TODO: consider making query for node and checking for response
    # but seems like it's rare to do this as a user, and nodes are mostly fetched in the
    # context of connection queries and other resolvers like allUserStatuses?


class ConnectionFilterFieldTestSuite(object):
    @pytest.fixture
    def field(self):
        '''This gets overwritten by inheriting class'''
        return None

    @pytest.fixture
    def model(self):
        '''This gets overwritten by inheriting class'''
        return None

    @pytest.fixture
    def graphene_client(self):
        return Client(schema)

    def count_nodes(self):
        res = self.graphene_client().execute(
            '''{
                allUserStatuses {
                    edges {
                        node {
                            id
                        }
                    }
                }
            }'''
        )
        return len(res['data'][self.field()]['edges'])

    def test_res_for_field_query__when_no_entries(self, field, model):
        '''Test that query for field returns 0 when no entries for the model exist.'''
        assert model.objects.count() == 0
        assert self.count_nodes() == model.objects.count()

    def test_res_for_field_query__when_entries(self, field, model):
        '''Test that query for field returns right number of nodes when entries for the model exist.'''
        n_entries_to_generate = 3
        mixer.cycle(n_entries_to_generate).blend(model)
        assert model.objects.count() == n_entries_to_generate
        assert self.count_nodes() == model.objects.count()
