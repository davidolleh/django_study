from django.db import models

class House(models.Model):
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)
    owenr = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name