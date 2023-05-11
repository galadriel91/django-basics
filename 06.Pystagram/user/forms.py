from django import forms
from django.core.exceptions import ValidationError
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3 , widget=forms.TextInput(attrs={"placeholder" : "사용자명 3자리 이상"}))
    password = forms.CharField(min_length=4 , widget=forms.PasswordInput(attrs={"placeholder": "비밀번호를 입력해주세요"}))

class SignupForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=4)
    password1 = forms.CharField(min_length=4)
    profile_image = forms.ImageField()
    short_description = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username = username).exists():
            raise ValidationError('이미 존재하는 사용자 입니다')
        return username
    
    def clean(self):
        password = self.cleaned_data['password']
        password1 = self.cleaned_data['password1']
        if password != password1:
            self.add_error('password1' , '비밀번호가 맞지않습니다')

    def save(self):
        username = self.cleaned_data['username']
        password1 = self.cleaned_data['password1']
        profile_image = self.cleaned_data['profile_image']
        short_description = self.cleaned_data['short_description']
        user = User.objects.create_user(
            username = username,
            password = password1,
            profile_image = profile_image,
            short_description = short_description,
        )
        return user