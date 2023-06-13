from django.urls import path
from .views import feed_view

urlpatterns = [
    path('feeds/', feed_view),
]

