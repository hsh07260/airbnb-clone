from django.db import models
from core import models as core_models


class List(core_models.AbstractTimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    room = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return f"{self.user} - {self.name}"

    def count_rooms(self):
        return self.room.count()

    count_rooms.short_description = "Number Of Rooms"
