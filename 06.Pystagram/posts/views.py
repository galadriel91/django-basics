from django.shortcuts import render
from .models import Post, PostImage, Comment

# Create your views here.
def feedView(request):
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request, 'posts/feeds_view.html' , context)