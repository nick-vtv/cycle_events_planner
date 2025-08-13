from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_image_size(image):
    if image.size > 1024 * 1024 * 5:
        raise ValidationError('The maximum size of the image is 5 MB')


def validate_photo_size(photo):
    if photo.size > 1024 * 1024 * 10:
        raise ValidationError('The maximum size of the photo is 10 MB')


def validate_current_date(value):
    if value < timezone.now().date():
        raise ValidationError("The date cannot be in the past.")
