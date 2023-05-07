from django.shortcuts import render

# Create your views here.

def main_list(request):
    return render(request, 'photo/photo_list.html')