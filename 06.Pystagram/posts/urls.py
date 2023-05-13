from django.urls import path
from .views import feeds_view

urlpatterns = [
    path('feed/', feeds_view, name='Feeds'),
]
