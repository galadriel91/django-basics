from django.shortcuts import render

from burger.models import Burger


def burgerList(request):
    burgers = Burger.objects.all()
    context={
        'burgers': burgers
    }
    return render(request, 'list.html', context)

def burgerMain(request):
    return render(request, 'main.html')

def burgerSearch(request):
    title = request.GET.get('title')
    if title is not None:
        item = Burger.objects.filter(title__contains=title)
    else:
        item = Burger.objects.none()
    context = {
        'item':item
    }
    return render(request, 'search.html' , context)