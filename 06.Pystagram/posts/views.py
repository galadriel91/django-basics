from django.shortcuts import render, redirect
from .models import Post, PostImage, Comment
from .forms import CommentForm, PostForm

# Create your views here.
def feedView(request):
    forms = CommentForm()
    posts = Post.objects.all()
    context={'posts':posts , 'forms':forms}
    return render(request, 'posts/feeds_view.html' , context)

def addForm(request):
    if request.method == 'POST':
        forms = CommentForm(data=request.POST)
        if forms.is_valid():
            comment = forms.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('Feeds')

def removeForm(request , id):
    if request.method == 'POST':
        forms = Comment.objects.get(id = id)
        forms.delete()
        return redirect('Feeds')
    
def addPost(request):
    if request.method == 'POST':
        forms = PostForm(data=request.POST, files=request.FILES)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.user = request.user
            post.save()

            for image in request.FILES.getlist('images'):
                PostImage.objects.create(
                    post = post,
                    photo = image
                )
            
            return redirect('Feeds')    
    else:
        forms = PostForm()
    context={'forms':forms}
    return render(request, 'posts/add_feeds.html', context)    