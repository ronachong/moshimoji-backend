from django.db import models

from project.gql_platform.models.content.serialization import base

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Serialization(base.Serialization):
    ''' attributes from base:
        - title
        - # author - noop
        check base class for more attributes or for changes
    '''
    genres = models.ManyToManyField(Genre)
#
# class Issue(base.Issue):
#     ''' attributes from base:
#         - title
#         - publication_date
#         - serialization
#         check base class for more attributes or for changes
#     '''
#     print_publication_date = models.DateTimeField()
#
# class Page(models.Model):
#     # how to make sure that each page has a sequential id?
#     issue = models.ForeignKey(Issue)
