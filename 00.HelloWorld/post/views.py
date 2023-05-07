from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def main_list(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request, 'photo/photo_list.html', context)

def main_item(request , pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post":post
    }
    return render(request, 'photo/photo_detail.html', context)