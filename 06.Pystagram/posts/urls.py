from django.urls import path
from .views import feeds_view, comment_add, comment_delete , post_add, tags_view

urlpatterns = [
    path('feed/', feeds_view, name='Feeds'),
    path('comment_add/', comment_add, name='CommentAdd'),
    path('comment_delete/<int:comment_id>/', comment_delete, name='CommentDelete'),
    path('add/', post_add, name='PostAdd'),
    path('tags/<str:tag_name>/', tags_view, name='TagsView')
]
