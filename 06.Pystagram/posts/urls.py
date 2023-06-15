from django.urls import path
from .views import feeds_view, add_comment, remove_comment, add_post

urlpatterns = [
    path('feeds/', feeds_view, name='feeds'),
    path('add_comment/', add_comment, name='addComment'),
    path('add_post/', add_post, name='addPost'),
    path('remove_comment/<int:comment_id>', remove_comment, name='removeComment'),
]
