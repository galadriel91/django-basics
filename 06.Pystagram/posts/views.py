from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def feeds_view(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    posts = Post.objects.all()
    context={"posts" : posts}
    return render(request, 'posts/feeds_view.html', context)