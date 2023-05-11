from django.shortcuts import render , redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

def feed_view(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form':comment_form
    }
    return render(request, 'post/feed_view.html', context)

@require_POST
def comment_add(request):
    forms = CommentForm(data = request.POST)
    if forms.is_valid():
        comment = forms.save(commit=False)
        comment.user = request.user
        comment.save()
        return HttpResponseRedirect(f'/post/feed/#post-{comment.post.id}')
    
@require_POST
def comment_remove(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    if comment.user == request.user:
        comment.delete()
        return HttpResponseRedirect(f'/post/feed/#post-{comment.post.id}')
    else:
        return HttpResponseForbidden('이 댓글을 삭제할 권한이 없습니다')
