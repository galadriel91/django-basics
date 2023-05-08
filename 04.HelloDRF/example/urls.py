from django.urls import path, include
from .views import HelloApi, BooksApi, BookApi

urlpatterns = [
    path('hello/', HelloApi),
    path('fbv/books/', BooksApi),
    path('fbv/books/<int:bid>/', BookApi),
]
