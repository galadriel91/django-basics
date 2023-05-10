from django.urls import path
from .views import TodosAPIView, TodoAPIView, DoneAPIView, DoneEditAPIView

urlpatterns = [
    path('', TodosAPIView.as_view()),
    path('<int:pk>/', TodoAPIView.as_view()),
    path('done/', DoneAPIView.as_view()),
    path('done/<int:pk>/', DoneEditAPIView.as_view()),
]
