from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

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

def main_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('main_item', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'photo/photo_new.html' , {'form':form})