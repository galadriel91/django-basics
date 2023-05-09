from django.urls import path
from .views import TodosAPIView, TodoAPIView, TodoDoneAPIView, CheckDoneAPIView

urlpatterns = [
    path('' , TodosAPIView.as_view()),
    path('<int:pk>/' , TodoAPIView.as_view()),
    path('done/', TodoDoneAPIView.as_view()),
    path('done/<int:pk>', CheckDoneAPIView.as_view())
]
