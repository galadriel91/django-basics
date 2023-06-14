from django.shortcuts import render

# Create your views here.

def feed_view(request):
    return render(request, 'posts/feed_view.html')