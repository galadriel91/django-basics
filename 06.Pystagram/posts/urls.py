from django.urls import path
from .views import feedView

urlpatterns = [
    path('feeds/', feedView, name="Feeds"),
]
