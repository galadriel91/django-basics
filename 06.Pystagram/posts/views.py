from django.shortcuts import render

# Create your views here.
def feeds_view(request):
    return render(request, 'posts/feeds_view.html')