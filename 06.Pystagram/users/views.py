from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import User
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if(user):
                login(request, user)
                return redirect('feeds')
            else:
                form.add_error(None , '로그인에 실패했습니다.')
        context= {
            'form' : form
        }
        return render(request , 'login_view.html' , context)
    else:
        form = LoginForm()
        context= {
            'form' : form
        }
        return render(request , 'login_view.html' , context)
    
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password1 = form.cleaned_data['password1']
            profile_image = form.cleaned_data['profile_image']
            short_desc = form.cleaned_data['short_desc']

            if password != password1:
                form.add_error('password1' , '비밀번호가 맞지 않습니다.')

            if User.objects.filter(username = username).exists():
                form.add_error('username', '이미 존재하는 사용자입니다.')

            if form.errors:
                context={
                    'form':form
                }    
                return render(request, 'signup_view.html' , context)
            else:
                user = User.objects.create_user(
                    username = username,
                    password = password1,
                    profile_image = profile_image,
                    short_desc = short_desc
                )
                login(request , user)
                return redirect('feeds')
    else:
        form = SignupForm()
        context= {
            'form' : form
        }
        return render(request, 'signup_view.html' , context)