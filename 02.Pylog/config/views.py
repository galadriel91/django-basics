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

def detail(request):
    return render(request , 'detail.html')

def add(request):
    return render(request , 'add.html')