from django.contrib.auth import get_user_model
from django.db import models

from routes.models import Route

UserModel = get_user_model()

# Create your models here.
class Event(models.Model):
    name = models.CharField(
        max_length=100,
    )

    route = models.ForeignKey(
        to=Route,
        on_delete=models.CASCADE,
        related_name='route_events',
    )

    event_date = models.DateField()

    event_time = models.TimeField()

    description = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='user_events',
    )

    def __str__(self):
        return self.name
