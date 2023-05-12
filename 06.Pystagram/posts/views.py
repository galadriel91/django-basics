from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Post
from .forms import CommentForm

# Create your views here.
def feeds_view(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    comment_form = CommentForm()
    posts = Post.objects.all()
    context={"posts" : posts , "comment_form":comment_form}
    return render(request, 'posts/feeds_view.html', context)

@require_POST
def comment_view(request):
    forms = CommentForm(data = request.POST)
    if forms.is_valid:
        comment = forms.save(commit=False)
        comment.user = request.user
        comment.save()
    return redirect(f'/posts/feeds/#post-{comment.post.id}')
