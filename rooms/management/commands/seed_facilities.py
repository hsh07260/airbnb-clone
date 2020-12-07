from django.core.management.base import BaseCommand
from rooms.models import Facilities


class Command(BaseCommand):

    help = "This command creates facilities"

    def handle(self, *args, **options):
        facilities = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
        ]
        for f in facilities:
            Facilities.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
