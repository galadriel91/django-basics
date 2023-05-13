from django.urls import path
from .views import feeds_view, comment_add, comment_delete

urlpatterns = [
    path('feed/', feeds_view, name='Feeds'),
    path('comment_add/', comment_add, name='CommentAdd'),
    path('comment_delete/<int:comment_id>', comment_delete, name='CommentDelete'),
]
