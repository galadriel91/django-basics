from django.urls import path
from .views import feedView, addForm, removeForm, addPost

urlpatterns = [
    path('feeds/', feedView, name="Feeds"),
    path('add_form/', addForm, name="AddForm"),
    path('remove_form/<int:id>/', removeForm, name="RemoveForm"),
    path('add_post/', addPost, name="AddPost"),
]
