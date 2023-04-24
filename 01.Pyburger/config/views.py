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