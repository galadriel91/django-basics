from django.shortcuts import render, redirect
from .models import Post, PostImage, Comment
from .forms import CommentForm

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
