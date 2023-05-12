from django.urls import path
from .views import feeds_view, comment_view

urlpatterns = [
    path('feeds/', feeds_view, name='Feeds'),
    path('comment_add/', comment_view, name='CommentAdd'),
]
