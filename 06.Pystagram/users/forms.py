from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': '사용자명(3글자 이상)'}),
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.TextInput(attrs={'placeholder': '비밀번호(4글자 이상)'}),
    )

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    profile_image = forms.ImageField()
    short_desc = forms.CharField()