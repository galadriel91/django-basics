from django.shortcuts import render
from .models import Post

# Create your views here.
def feeds_view(request):
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request, 'posts/feeds_view.html' , context)