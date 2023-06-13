from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)
            if user:
                login(request , user)
                return redirect('feeds')
            else:
                form.add_error(None, '로그인에 실패 하였습니다.')
        context={
            'form':form
        }
        return render(request, 'login_view.html' , context)
    else:
        form = LoginForm()
        context={
            'form':form
        }
        return render(request, 'login_view.html' , context)
    

def logout_view(request):
    logout(request)
    return redirect('login')