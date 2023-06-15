from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm

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