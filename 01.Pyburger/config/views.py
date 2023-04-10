from django.shortcuts import render

from burger.models import Burger


def main(requeset):
    return render(requeset , 'main.html')

def lists(request):
    burgers = Burger.objects.all()
    context = {
        'burgers': burgers
    }
    return render(request , 'list.html' , context)

def search(requeset):
    keyword = requeset.GET.get('keyword')
    if keyword is not None :
        item = Burger.objects.filter(title__contains = keyword)
    else:
        item = Burger.objects.none()
    context = {
        'item': item
    }
    return render(requeset, 'search.html', context)