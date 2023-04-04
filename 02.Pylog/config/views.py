from django.shortcuts import render

def main(request):
    return render(request , 'main.html')

def post(request):
    return render(request , 'post.html')

def detail(request):
    return render(request , 'detail.html')

def add(request):
    return render(request , 'add.html')