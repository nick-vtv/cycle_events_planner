from django.contrib.auth import get_user_model
from django.db import models

from common.validators import validate_photo_size
from events.models import Event

UserModel = get_user_model()

# Create your models here.
class Photo(models.Model):
    event_photo = models.ImageField(
        upload_to='upload/gallery/',
        validators=[validate_photo_size, ],
    )

    to_event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name='photos',
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='gallery_photos',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Photo {self.pk} by {self.created_by.profile} for event {self.to_event}'
