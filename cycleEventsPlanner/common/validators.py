from django.core.exceptions import ValidationError


def validate_image_size(image):
    if image.size > 1024 * 1024 * 10:
        raise ValidationError('The maximum size of the image is 10 MB')
