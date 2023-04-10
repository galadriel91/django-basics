from django.shortcuts import render


def main(requeset):
    return render(requeset , 'main.html')