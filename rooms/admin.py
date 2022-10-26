from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def resetPrices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (
        resetPrices,
    )

    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "total_amenities",
        "rating",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities"
    )

    search_fields = (
        "^name",
        "=price",
        "owner__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at"
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
