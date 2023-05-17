from django.shortcuts import render, redirect
from .models import Post, PostImage, Comment, HashTag
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

            tag_string = request.POST.get('tags')    
            tag_names = [tag_name.strip() for tag_name in tag_string.split(',')]
            for tag_name in tag_names:
                tag,_ = HashTag.objects.get_or_create(name = tag_name)
                post.tags.add(tag)
            
            return redirect('Feeds')    
    else:
        forms = PostForm()
    context={'forms':forms}
    return render(request, 'posts/add_feeds.html', context)    

def tagsResult(request, tagName):
    try:
        tag = HashTag.objects.get(name = tagName)
    except HashTag.DoesNotExist:
        posts = Post.objects.none()
    else:
        posts = Post.objects.filter(tags = tag)    
    context={'tagName':tagName, 'posts':posts}
    return render(request, 'posts/tags.html', context)