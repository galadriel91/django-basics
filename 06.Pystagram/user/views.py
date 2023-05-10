from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('Feed')
    else:
        return render(request, 'user/login_view.html')
        