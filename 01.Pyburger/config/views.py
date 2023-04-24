from django.shortcuts import render


def burgerList(request):
    return render(request, 'list.html')