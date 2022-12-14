from pyexpat import model
from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    country = models.CharField(max_length=50, default='한국')
    city = models.CharField(max_length=80, default='서울')
    name = models.CharField(max_length=150, default='defalut')
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey(
        "users.User",
        related_name="rooms",
        on_delete=models.CASCADE
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms"
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name="rooms",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        return self.amenities.count()

    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0.0
            for rating in self.reviews.all().values("rating"):
                total_rating += rating['rating']
            return round(total_rating / count, 2)


class Amenity(CommonModel):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
