from tabnanny import verbose
from django.db import models
from common.models import CommonModel

class Category(CommonModel):
    
    class CategorykindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCE = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=30, choices=CategorykindChoices.choices)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"