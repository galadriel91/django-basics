from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('Feeds')
    
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)

            if user:
                login(request, user)
                return redirect('Feeds')
            else:
                form.add_error(None, "로그인에 실패했습니다.")
        context = {
            'form' : form
        }
        return render(request, 'users/login.html', context)        
    else:
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('Login')