from django.db import models
from misago.users.models.user import User as MisagoUser
import logging

logger = logging.getLogger('django')

# Create your models here.
class UserStatus(models.Model):
    user = models.ForeignKey(MisagoUser)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
