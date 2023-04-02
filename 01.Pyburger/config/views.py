from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request , 'main.html')

def burger(request):
    burger = Burger.objects.all()
    context = {
        "burgers" : burger
    }
    return render(request , 'burger.html' , context)

def search(request):
    keyword = request.GET.get('keyword')
    if keyword is not None:
        burger = Burger.objects.filter(name__contains = keyword)
    else:
        burger = Burger.objects.none()
    context = {
        "burger" : burger
    }
    return render(request , 'search.html' , context)
