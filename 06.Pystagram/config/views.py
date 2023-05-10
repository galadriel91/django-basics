from django.shortcuts import redirect

def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('Feeds')
    else:
        return redirect('Login')