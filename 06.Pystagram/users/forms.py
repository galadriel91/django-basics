from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=4 , widget=forms.TextInput(attrs={'placeholder':'사용자명(3글자 이상)'}))
    password = forms.CharField(min_length=3 , widget=forms.PasswordInput(attrs={'placeholder':'비밀번호(5글자 이상)'}))

class SignupForm(forms.Form):
    username = forms.CharField(min_length=3)    
    password = forms.CharField(min_length=5)    
    password1 = forms.CharField(min_length=5)    
    profile_image = forms.ImageField()    
    short_description = forms.CharField()    