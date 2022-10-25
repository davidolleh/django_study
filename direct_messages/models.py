from django.db import models
from common.models import CommonModel


# Create your models here.
class ChattingRoom(CommonModel):
    users = models.ManyToManyField(
        "users.User",
        related_name='chattingRooms',
    )

    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        related_name='messages',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        related_name='messages',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} says {self.text}"
