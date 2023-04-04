from django.shortcuts import render , redirect
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
    if request.method == 'POST':
        Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('/posts/')
    return render(request , 'add.html')