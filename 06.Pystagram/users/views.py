from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('Feeds')
    return render(request, 'users/login.html')