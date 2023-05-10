from django.shortcuts import render, redirect

# Create your views here.

def feeds(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('Login')
    return render(request, 'posts/feeds.html')