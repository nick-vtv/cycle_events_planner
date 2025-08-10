from django import forms

from routes.models import Route


class RouteBaseForm(forms.ModelForm):
    class Meta:
        model = Route
        exclude = ['created_by', 'created_at', ]
        labels = {
            'name': 'Route Name',
            'difficulty': 'Difficulty',
            'type': 'Route Type',
            'description': 'Brief Description',
            'distance': 'Route Distance',
            'start_point': 'Route Start Point',
            'end_point': 'Route End Point',
            'is_circular': 'Is this a circular route?',
            'map_image': 'Link to Map Image',
            'route_photo': 'Upload a Route Photo',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your route name:'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Some description... (optional):'
                }
            ),
            'distance': forms.NumberInput(
                attrs={
                    'placeholder': 'Route distance (in KM) (optional):'
                }
            ),
            'start_point': forms.TextInput(
                attrs={
                    'placeholder': 'Start point location or GPS coordinates:'
                }
            ),
            'end_point': forms.TextInput(
                attrs={
                    'placeholder': 'End point location or GPS coordinates:'
                }
            ),
            'map_image': forms.TextInput(
                attrs={
                    'placeholder': 'Link to a map image (optional):'
                }
            ),
            'route_photo' : forms.FileInput(),
        }


class RouteCreateForm(RouteBaseForm):
    pass


class RouteEditForm(RouteBaseForm):
    pass


class RouteDeleteForm(RouteBaseForm):
    pass
