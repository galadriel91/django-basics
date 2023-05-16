from django.urls import path
from .views import feedView, addForm, removeForm

urlpatterns = [
    path('feeds/', feedView, name="Feeds"),
    path('add_form/', addForm, name="AddForm"),
    path('remove_form/<int:id>', removeForm, name="RemoveForm"),
]
