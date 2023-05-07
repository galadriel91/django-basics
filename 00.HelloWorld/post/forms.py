from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # 이 부분은 모르겠는데?
    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'image',
            'description',
            'price',
        )
