from django.contrib.auth import get_user_model
from django.db import models

from bikes.choices import BikeTypeChoices, BikeGeometryChoices

UserModel = get_user_model()

# Create your models here.
class Bike(models.Model):
    manufacturer = models.CharField(
        max_length=50,
    )

    model = models.CharField(
        max_length=50,
    )

    type = models.CharField(
        max_length=50,
        choices=BikeTypeChoices.choices,
        default=BikeTypeChoices.MTB
    )

    geometry = models.CharField(
        max_length=100,
        choices=BikeGeometryChoices.choices,
        default=BikeGeometryChoices.HARDTAIL,
    )

    is_ebike = models.BooleanField(
        default=False,
    )

    year = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    wheel_size = models.FloatField(
        null=True,
        blank=True,
    )

    is_mullet = models.BooleanField(
        default=False,
    )

    weight = models.FloatField(
        null=True,
        blank=True,
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='bikes',
    )

    def __str__(self):
        return f'{self.manufacturer} {self.model}'
