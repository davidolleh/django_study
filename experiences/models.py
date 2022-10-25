from tkinter import CASCADE
from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    country = models.CharField(max_length=50, default='한국')
    city = models.CharField(max_length=80, default='서울')
    name = models.CharField(max_length=150)
    description = models.TextField()
    host = models.ForeignKey(
        "users.User",
        related_name='experiences',
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=150)
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name='experiences',
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name='experiences',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=250, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
