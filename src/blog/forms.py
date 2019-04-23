from django import forms
from .models import Comment


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
