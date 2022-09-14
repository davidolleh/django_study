from django.contrib import admin
from .models import Review

@admin.register(Review)
class Reviewadmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        "rating",
    )