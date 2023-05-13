from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.decorators.http import require_POST
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
def feeds_view(request):
    comment_form = CommentForm()
    posts = Post.objects.all()
    context={'posts':posts, 'comment_form': comment_form}
    return render(request, 'posts/feeds_view.html' , context)

@require_POST
def comment_add(request):
    forms = CommentForm(data = request.POST)
    if forms.is_valid():
        comment = forms.save(commit=False)
        comment.user = request.user
        comment.save()
        return redirect('Feeds')

@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.user == comment.user:
        comment.delete()
        return redirect('Feeds')
    else:
        return HttpResponseForbidden('이 게시글을 삭제 할 수 없습니다.')