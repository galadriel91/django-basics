from django.urls import path
from .views import feedView, addForm

urlpatterns = [
    path('feeds/', feedView, name="Feeds"),
    path('add_form/', addForm, name="AddForm"),
]
