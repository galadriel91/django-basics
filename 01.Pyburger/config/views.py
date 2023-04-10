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