from django.urls import path
from .views import feeds_view, comment_view, comment_delete, post_add, tags

urlpatterns = [
    path('feeds/', feeds_view, name='Feeds'),
    path('comment_add/', comment_view, name='CommentAdd'),
    path('comment_delete/<int:commentid>/', comment_delete, name='CommentDelete'),
    path('add/', post_add, name='PostAdd'),
    path('tags/<str:tag_name>', tags, name="Tags")
]
