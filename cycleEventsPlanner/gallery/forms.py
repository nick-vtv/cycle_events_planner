from django import forms

from gallery.models import Photo


class GalleryBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['created_by', 'created_at', ]
        labels = {
            'event_photo': 'Upload an Event Photo',
            'to_event': 'Choose an Event'
        }

        widgets = {
            'event_photo': forms.FileInput(),
        }


class GalleryPhotoAddForm(GalleryBaseForm):
    pass


class GalleryPhotoDeleteForm(GalleryBaseForm):
    pass
