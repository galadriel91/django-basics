from django.shortcuts import render
from .models import Burger
# Create your views here.

def burger_list(request):
    burgers = Burger.objects.all()
    context = {
        'burgers' : burgers
    }
    return render(request, 'burger_list.html' , context)