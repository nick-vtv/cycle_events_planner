from django import forms

from events.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['created_by', 'created_at', ]

        labels = {
            'name': 'Event Name',
            'route': 'Route Name',
            'event_date': 'Event Date',
            'event_time': 'Event Time',
            'description': 'Brief Description',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Your event name:'
                }
            ),
            'event_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'Choose event date:'
                }
            ),
            'event_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'placeholder': 'Choose event time:'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Some description... (optional):'
                }
            )
        }


class EventCreateForm(EventBaseForm):
    pass


class EventEditForm(EventBaseForm):
    pass


class EventDeleteForm(EventBaseForm):
    pass
