from django.shortcuts import render
from .models import Post

# Create your views here.

def main_list(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request, 'photo/photo_list.html', context)