from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")
    
    class CurrrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dolor"
  
    first_name = models.CharField(max_length=150, editable=False,)
    last_name = models.CharField(max_length=150, editable=False,)
    name = models.CharField(max_length=150, default="",)
    avater = models.ImageField(blank=True)
    is_host = models.BooleanField(default=False,)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices,)
    currency = models.CharField(max_length=5, choices=CurrrencyChoices.choices,)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,)