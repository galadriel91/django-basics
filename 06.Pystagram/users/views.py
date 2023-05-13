from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import LoginForm, SignupForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']

            user = authenticate(username=username, password = password)
            if user:
                login(request, user)
                return redirect('Feeds')
            else:
                forms.add_error(None, '로그인에 실패했습니다.')
        context = {'forms':forms}
        return render(request, 'users/login_view.html' , context)
    else:
        forms = LoginForm()
        context={'forms':forms}
        return render(request, 'users/login_view.html' , context)
    
def signup_view(request):

    if request.POST:
        forms = SignupForm(data = request.POST, files=request.FILES)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            password1 = forms.cleaned_data['password1']
            profile_image = forms.cleaned_data['profile_image']
            short_description = forms.cleaned_data['short_description']

            if password != password1:
                forms.add_error('password1' , '비밀번호가 맞지않습니다.')

            if User.objects.filter(username=username).exists():
                forms.add_error('username' , '이미 존재하는 사용자입니다.')
            
            if forms.errors:
                context={'forms':forms}
                return render(request, 'users/signup_view.html' , context)
            else:
                user = User.objects.create_user(
                    username = username,
                    password = password1,
                    profile_image = profile_image,
                    short_description = short_description
                )    
                login(request, user)
                return redirect('Feeds')
    else:
        forms = SignupForm()
        context={'forms':forms}
        return render(request, 'users/signup_view.html' , context)