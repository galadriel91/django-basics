from django.shortcuts import render

# Create your views here.

def burger_list(request):
    return render(request, 'burger_list.html')