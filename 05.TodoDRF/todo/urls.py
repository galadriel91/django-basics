from django.urls import path
from .views import TodosAPIView, TodoAPIView, DoneAPIView

urlpatterns = [
    path('', TodosAPIView.as_view()),
    path('<int:pk>/', TodoAPIView.as_view()),
    path('done/', DoneAPIView.as_view()),
]
