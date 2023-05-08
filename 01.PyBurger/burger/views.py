from django.shortcuts import render
from .models import Burger
# Create your views here.

def burger_list(request):
    burgers = Burger.objects.all()
    context = {
        'burgers' : burgers
    }
    return render(request, 'burger_list.html' , context)

def burger_search(request):
    keyword = request.GET.get('keyword')
    if keyword is not None:
        search = Burger.objects.filter(title__contains = keyword)
    else:
        search = Burger.objects.none()
    context={
        'search':search
    }
    return render(request, 'burger_search.html', context)