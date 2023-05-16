from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=5, widget=forms.TextInput(attrs={"placeholder":'사용자명(5자리 이상)'}))
    password = forms.CharField(min_length=3, widget=forms.PasswordInput(attrs={'placeholder':'비밀번호(3자리이상)'}))