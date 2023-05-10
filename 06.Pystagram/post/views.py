from django.shortcuts import render , redirect

# Create your views here.

def feed_view(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        return render(request, 'post/feed_view.html')