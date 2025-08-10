from django.contrib.auth import get_user_model
from django.db import models

from common.validators import validate_image_size
from routes.choices import RouteDifficultyChoices, RouteTypeChoices

UserModel = get_user_model()

# Create your models here.
class Route(models.Model):
    name = models.CharField(
        max_length=100,
    )

    difficulty = models.CharField(
        max_length=100,
        choices=RouteDifficultyChoices.choices,
        default=RouteDifficultyChoices.BEGINNER
    )

    type = models.CharField(
        max_length=150,
        choices=RouteTypeChoices.choices,
        default=RouteTypeChoices.AM
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    distance = models.FloatField(
        blank=True,
        null=True,
    )

    start_point = models.CharField(
        max_length=150,
    )

    end_point = models.CharField(
        max_length=150,
    )

    is_circular = models.BooleanField(
        default=False,
    )

    map_image = models.URLField(
        blank=True,
        null=True,
    )

    route_photo = models.ImageField(
        upload_to='upload/',
        validators=[validate_image_size, ],
        blank=True,
        null=True,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='routes',
    )

    def __str__(self):
        return self.name
