from django.shortcuts import render
from blog.models import Post

def main(request):
    return render(request , 'main.html')

def post(request):
    posts = Post.objects.all()
    context={
        "posts":posts
    }
    return render(request , 'post.html' , context)

def detail(request , post_id):
    post = Post.objects.get(id = post_id)
    context = {
        'post' : post
    }
    return render(request , 'detail.html' , context)

def add(request):
    return render(request , 'add.html')