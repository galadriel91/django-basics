from django.shortcuts import render , get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, 'post/post_list.html', context)
    
def post_detail(request , pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post" : post
    }
    return render(request, 'post/post_detail.html', context)    

def post_add(request):
    if request.method == 'POST':
        forms = PostForm(request.POST)
        if forms.is_valid:
            post = forms.save(commit=False)
            post.save()
            return redirect('post_detail' , pk=post.pk)
    else:
        forms = PostForm()    
    context = {
        'forms' : forms
    }
    return render(request, 'post/post_add.html', context)    

def post_edit(request , pk):
    detail = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        forms = PostForm(request.POST , instance=detail)
        if forms.is_valid:
            post = forms.save(commit=False)
            post.save()
            return redirect('post_detail' , pk=post.pk)
    else:
        forms = PostForm(instance=detail)    
    context = {
        'forms' : forms
    }
    return render(request, 'post/post_add.html', context)    