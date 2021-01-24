from django.db import models
from . import managers


class AbstractTimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomReservationManager()

    class Meta:
        abstract = True
