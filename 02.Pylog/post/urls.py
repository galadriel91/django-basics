from django.urls import path
from .views import PostList, PostDetail, PostAdd

urlpatterns = [
    path('', PostList, name='PostList'),
    path('<int:pk>/', PostDetail, name='PostDetail'),
    path('add/', PostAdd, name='PostAdd'),
]
