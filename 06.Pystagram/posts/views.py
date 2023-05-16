from django.shortcuts import render

# Create your views here.
def feedView(request):
    return render(request, 'posts/feeds_view.html')