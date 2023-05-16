from django.urls import path
from .views import BooksView, BookView

urlpatterns = [
    path('', BooksView.as_view()),
    path('<int:pk>', BookView.as_view()),
]
