from django.shortcuts import render, redirect

# Create your views here.
def feeds_view(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    return render(request, 'posts/feeds_view.html')