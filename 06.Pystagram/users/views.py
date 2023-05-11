from django.contrib.auth import login, logout , authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import User

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('Feeds')
    if request.method == 'POST':
        forms = LoginForm(data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']

            user = authenticate(username = username, password = password)
            
            if user:
                login(request, user)
                return redirect('Feeds')
            else:
                forms.add_error('로그인에 실패했습니다.')
        context={'forms':forms}
        return render(request, 'users/login_view.html' , context)                
    else:
        forms = LoginForm()
        context={'forms':forms}
        return render(request, 'users/login_view.html' , context)
    
def logout_view(request):
    logout(request)
    return redirect('Login')    

def signup_view(request):
    if request.method == 'POST':
        forms = SignupForm(data = request.POST, files=request.FILES)
        if forms.is_valid():
            user = forms.save()
            login(request , user)
            return redirect('Feeds')
        else:
            context = {'forms':forms}
            return render(request, 'users/signup_view.html', context)
    else:
        forms = SignupForm()
        context = {'forms':forms}
        return render(request, 'users/signup_view.html', context)
