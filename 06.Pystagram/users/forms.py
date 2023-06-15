from django import forms
from django.core.exceptions import ValidationError
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder':'사용자명(3자리 이상)'})
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(attrs={'placeholder':'비밀번호(4자리 이상)'})
    )
    

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_desc = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise ValidationError(f'입력한 사용자명({username})은 이미 존재하는 회원입니다.')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            self.add_error('password1' , '비밀번호가 맞지 않습니다.')

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        profile_image = self.cleaned_data['profile_image']
        short_desc = self.cleaned_data['short_desc']

        user = User.objects.create_user(
            username = username,
            password = password1,
            profile_image = profile_image,
            short_desc = short_desc
        )
        return user