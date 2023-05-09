from django.shortcuts import render, get_object_or_404 , redirect
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
    if request.method == 'POST':
        Comment.objects.create(
            post = post,
            content = request.POST['content']
        )
    context = {
        "post": post
    }
    return render(request, 'post_detail.html', context)

def PostAdd(request):
    if request.method == 'POST':
        Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            thumbnail = request.FILES['thumbnail']
        )
        return redirect('PostList')
    return render(request, 'post_add.html')