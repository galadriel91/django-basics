from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignupForm
from .models import User

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        forms = LoginForm(data = request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect('https://www.naver.com')
            else:
                forms.errors(None, '로그인에 실패했습니다.')
        else:
            context={'forms':forms}
            return render(request, 'users/login_view.html', context)                        
    else:
        forms = LoginForm()
        context={'forms':forms}
        return render(request, 'users/login_view.html', context)
    
def signupView(request):
    if request.method == 'POST':
        forms = SignupForm(data = request.POST, files=request.FILES)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            password1 = forms.cleaned_data['password1']
            profile_image = forms.cleaned_data['profile_image']
            description = forms.cleaned_data['description']

        if password != password1:
            forms.add_error('password1' , '비밀번호가 맞지 않습니다.')

        if User.objects.filter(username = username).exists():
            forms.add_error('username', '이미 존재하는 사용자 입니다.')

        if forms.errors:
            context={'forms':forms}
            return render(request, 'users/signup_view.html', context)    
        else:
            user = User.objects.create_user(
                username = username,
                password = password1,
                profile_image = profile_image,
                description = description
            )
            login(request, user)
            # return render(request, 'users/signup_view.html', context) 
            return redirect('https://www.naver.com')    

    else:
        forms = SignupForm()
        context={'forms':forms}
        return render(request, 'users/signup_view.html', context)