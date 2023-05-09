from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList, name='PostList'),
    path('<int:pk>/', PostDetail, name='PostDetail'),
]
