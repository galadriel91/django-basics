from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import Post, Comment, PostImage, HashTag
from .forms import CommentForm, PostForm

# Create your views here.
def feeds_view(request):
    posts = Post.objects.all()
    form = CommentForm()
    context={
        'posts':posts,
        'form':form
    }
    return render(request , 'posts/feeds_view.html', context)

@require_POST
def add_comment(request):
    form = CommentForm(data = request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
        return redirect('feeds')
    
@require_POST
def remove_comment(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.user == comment.user:
        comment.delete()
        return redirect('feeds')
    
def add_post(request): 
    if request.method == 'POST':
        form = PostForm(data = request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            for image_file in request.FILES.getlist('images'):
                PostImage.objects.create(
                    post = post,
                    photo = image_file
                )

            tag_string = request.POST.get('tags')
            if tag_string:
                tag_names = [tag_name.strip() for tag_name in tag_string.split(',')]
                for tag_name in tag_names:
                    tag,_ =  HashTag.objects.get_or_create(name = tag_name)
                    post.tag.add(tag)
            return redirect('feeds')
    else:
        form = PostForm()
    context={
        'form' : form
    }
    return render(request, 'posts/add_post.html' , context)


def tags(request , tag_name):
    try:
        tag = HashTag.objects.get(name = tag_name)
    except HashTag.DoesNotExist:
        posts = Post.objects.none()
    else:
        posts = Post.objects.filter(tag = tag)
    context = {
        'name' : tag_name,
        'posts':posts
    }
    return render(request , 'posts/tags.html' , context)
