from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

# Create your views here.

def PostList(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'post_list.html', context)

def PostDetail(request , pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post
    }
    return render(request, 'post_detail.html', context)