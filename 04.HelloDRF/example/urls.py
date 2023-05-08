from django.urls import path, include
from .views import BooksApi, BookApi

urlpatterns = [
    path('fbv/books/', BooksApi.as_view()),
    path('fbv/books/<int:bid>/', BookApi.as_view()),
]
