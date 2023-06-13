from django.shortcuts import render

# Create your views here.

def feed_view(request):
    return render(request, 'feed_view.html')