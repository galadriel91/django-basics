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
    burger = Burger.objects.filter(name__contains = keyword)
    context = {
        "burger" : burger
    }
    return render(request , 'search.html' , context)
