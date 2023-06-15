from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'post',
            'content'
        ]
        widgets = {
            'content' : forms.Textarea(
                attrs={'placeholder' : '댓글달기..'}
            )
        }