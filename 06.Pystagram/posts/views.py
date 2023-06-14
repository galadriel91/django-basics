from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

def feed_view(request):
    posts = Post.objects.all()
    form = CommentForm()
    context={
        'posts': posts,
        'form' : form
    }
    return render(request, 'posts/feed_view.html' , context)

@require_POST
def comment_add(request):
    form = CommentForm(data = request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
        return redirect('feeds')
    
@require_POST
def remove_comment(request , comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id = comment_id)
        if comment.user == request.user:
            comment.delete()
            return redirect('feeds')
