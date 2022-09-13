from django.contrib import admin
from .models import Room, Amenity

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "price",
        "kind",
        "owner",
        "created_at",
        "updated_at"
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
class AmentyAdmin(admin.ModelAdmin):
    pass

