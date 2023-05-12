from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect
from .models import Post, Comment, PostImage
from .forms import CommentForm, PostForm

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
    return HttpResponseRedirect(f'/posts/feeds/#post-{comment.post.id}')

@require_POST
def comment_delete(request, commentid):
    comment = Comment.objects.get(id = commentid)
    if comment.user == request.user:
        comment.delete()
        return HttpResponseRedirect(f'/posts/feeds/#post-{comment.post.id}')
    else:
        return HttpResponseRedirect('이 댓글을 삭제할 권한이 없습니다.')

def post_add(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            for image_file in request.FILES.getlist('images'):
                PostImage.objects.create(
                    post = post,
                    photo = image_file
                )
            return HttpResponseRedirect(f'/posts/feeds/#post-{post.id}')
    else:
        form = PostForm()
        context={'form' : form}
        return render(request, 'posts/post_add.html' , context)