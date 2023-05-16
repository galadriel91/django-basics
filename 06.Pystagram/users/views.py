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
                return redirect('Feeds')
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
            user = forms.save()
            login(request, user)
            return redirect('Feeds')
    else:
        forms = SignupForm()
    context={'forms':forms}
    return render(request, 'users/signup_view.html', context)

def logoutView(requet):
    logout(requet)
    return redirect('Login')