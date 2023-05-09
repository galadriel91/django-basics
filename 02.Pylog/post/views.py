from django.shortcuts import render
from .models import Post, Comment

# Create your views here.

def PostList(request):
    return render(request, 'post_list.html')