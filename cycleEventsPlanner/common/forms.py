from django import forms

from common.models import Comment

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Add a comment...'
                }
            )
        }
