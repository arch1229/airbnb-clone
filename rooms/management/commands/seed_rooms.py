import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This command creates dummy rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms do you create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "guests": lambda x: random.randint(1, 5),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(1, 500000),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        created_rooms_id = flatten(list(created_rooms.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
        for pk in created_rooms_id:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 31)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    image_file=f"room_photos/{random.randint(1,31)}.webp",
                )
            for a in amenities:
                magic_number = random.randint(0, 30)
                if magic_number % 3 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 30)
                if magic_number % 3 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 30)
                if magic_number % 3 == 0:
                    room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} dummy rooms created!"))
