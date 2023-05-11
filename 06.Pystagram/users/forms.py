from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=4)

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password1 = forms.CharField()
    profile_image = forms.ImageField()
    short_description = forms.CharField()