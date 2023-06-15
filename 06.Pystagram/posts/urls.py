from django.urls import path
from .views import feeds_view, add_comment

urlpatterns = [
    path('feeds/', feeds_view, name='feeds'),
    path('add_comment/', add_comment, name='addComment'),
]
