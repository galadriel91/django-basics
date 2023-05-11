from django.urls import path 
from .views import feed_view, comment_add, comment_remove

urlpatterns = [
    path('feed/', feed_view, name='Feed'),
    path('comment_add/', comment_add, name='CommentAdd'),
    path('comment_remove/<int:comment_id>/', comment_remove, name='CommentRemove'),
]
