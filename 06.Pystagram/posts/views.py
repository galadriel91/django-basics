from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.decorators.http import require_POST
from .models import Post, Comment, PostImage, HashTag
from .forms import CommentForm, PostForm

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
    
def post_add(request):
    if request.method == 'POST':
        forms = PostForm(data=request.POST)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.user =request.user
            post.save()

            for image in request.FILES.getlist('images'):
                PostImage.objects.create(
                    post = post,
                    photo = image
                )

            tag_string = request.POST.get('tags')
            if tag_string:
                tag_names = [tag_name.strip() for tag_name in tag_string.split(',')]
                for tag_name in tag_names:
                    tag, _ = HashTag.objects.get_or_create(name = tag_name)
                    post.tags.add(tag)
            return redirect('Feeds')    
    else:
        forms = PostForm()
        context={'forms':forms}
        return render(request, 'posts/post_add.html', context)    
    

def tags_view(request , tag_name):
    try:
        tag = HashTag.objects.get(name = tag_name)
    except HashTag.DoesNotExist:
        posts= Post.objects.none()
    else:
        posts = Post.objects.filter(tags = tag)
    context={'tag_name':tag_name, 'posts':posts}
    return render(request, 'posts/tags.html', context)