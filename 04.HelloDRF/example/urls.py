from django.urls import path, include
from .views import HelloApi

urlpatterns = [
    path('hello/', HelloApi),
]
