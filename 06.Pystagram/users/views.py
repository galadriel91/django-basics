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
            user = forms.save()
            login(request, user)
            return redirect('Feeds')
    else:
        forms = SignupForm()
    context={'forms':forms}
    return render(request, 'users/signup_view.html' , context)

def logout_view(request):
    logout(request)
    return redirect('Login')