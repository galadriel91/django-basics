from django.contrib import admin
from django.urls import path
from .views import feed_view , comment_add , remove_comment

urlpatterns = [
    path('feeds/', feed_view, name='feeds'),
    path('comment_add/', comment_add, name='commentAdd'),
    path('comment_remove/<int:comment_id>', remove_comment, name='removeComment'),
]
