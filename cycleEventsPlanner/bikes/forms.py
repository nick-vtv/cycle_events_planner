from django import forms

from bikes.models import Bike


class BikeBaseForm(forms.ModelForm):
    class Meta:
        model = Bike
        exclude = ['user', ]
        labels = {
            'manufacturer': 'Bike Manufacturer',
            'model': 'Model Name',
            'type': 'Bike Type',
            'geometry': 'Bike Geometry',
            'is_ebike': 'Is this an E-Bike?',
            'year': 'Year Produced',
            'wheel_size': 'Wheel Size',
            'is_mullet': 'Is this a Mullet? (front and rear wheel sizes are different)',
            'weight': 'Weight',
            'picture': 'Link to photo',
        }

        widgets = {
            'manufacturer': forms.TextInput(
                attrs={
                    'placeholder': 'Your bike manufacturer brand:'
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'placeholder': 'Your bike model name:'
                }
            ),
            'year': forms.NumberInput(
                attrs={
                    'placeholder': 'Your bike year of production:'
                }
            ),
            'wheel_size': forms.NumberInput(
                attrs={
                    'placeholder': 'Your bike wheel size (in INCHES):'
                }
            ),
            'weight': forms.NumberInput(
                attrs={
                    'placeholder': 'Your bike weight (in KGS):'
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Link to an image of your bike:'
                }
            )
        }


class BikeCreateForm(BikeBaseForm):
    pass


class BikeEditForm(BikeBaseForm):
    pass


class BikeDeleteForm(BikeBaseForm):
    pass
