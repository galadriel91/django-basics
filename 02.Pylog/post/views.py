from django.shortcuts import render
from .models import Post, Comment

# Create your views here.

def PostList(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'post_list.html', context)