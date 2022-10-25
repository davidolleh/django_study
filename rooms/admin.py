from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "total_amenities",
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

    readonly_fields = (
        "created_at",
        "updated_at"
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass
