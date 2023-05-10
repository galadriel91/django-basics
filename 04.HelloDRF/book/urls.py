from django.urls import path
from .views import BooksAPIView, BookAPIView

urlpatterns = [
    path('', BooksAPIView.as_view()),
    path('<int:pk>', BookAPIView.as_view()),
]
