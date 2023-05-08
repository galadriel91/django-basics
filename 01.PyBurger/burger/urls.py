from django.urls import path, include
from .views import burger_list, burger_search

urlpatterns = [
    path('', burger_list),
    path('search/', burger_search),
]
