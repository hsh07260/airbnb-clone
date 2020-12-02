from django.db import models
from core import models as core_models


class Review(core_models.AbstractTimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.PositiveIntegerField()
    communication = models.PositiveIntegerField()
    cleanliness = models.PositiveIntegerField()
    location = models.PositiveIntegerField()
    check_in = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6

        return round(avg, 2)

    rating_average.short_description = "Avg"

    def __str__(self):
        return f"{self.review} - {self.room}"
