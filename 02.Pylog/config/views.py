from django.shortcuts import render , redirect
from blog.models import Post, Comment

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
    if request.method == 'POST':
        Comment.objects.create(
            post = post,
            content = request.POST['comment']
        )
    context = {
        'post' : post
    }
    return render(request , 'detail.html' , context)

def add(request):
    if request.method == 'POST':
        Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            thumbnail = request.FILES['thumbnail']
        )
        return redirect('/posts/')
    return render(request , 'add.html')