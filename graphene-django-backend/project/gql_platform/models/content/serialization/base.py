from django.db import models
# from project.gql_platform.models.content.base import Author

class Serialization(models.Model):
    title = models.CharField(max_length=150)
    # author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

# class Issue(models.Model):
#     title = models.CharField(max_length=1000)
#     site_publication_date = models.DateTimeField(auto_now_add=True)
#     serialization = models.ForeignKey(Serialization)
#
#     class Meta:
#         abstract = True

pass
