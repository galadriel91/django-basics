from django.shortcuts import render
from .models import Post
# Create your views here.

def feed_view(request):
    posts = Post.objects.all()
    context={
        'posts': posts
    }
    return render(request, 'posts/feed_view.html' , context)