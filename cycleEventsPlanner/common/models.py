from django.contrib.auth import get_user_model
from django.db import models

from events.models import Event

UserModel = get_user_model()

# Create your models here.
class Comment(models.Model):
    for_event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name='event_comments',
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='user_comments',
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    comment = models.TextField()

