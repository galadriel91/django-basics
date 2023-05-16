from django.shortcuts import redirect

def index(request):
    if request.user:
        return redirect('Feeds')
    else:
        return redirect('Login')