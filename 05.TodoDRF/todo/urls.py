from django.urls import path
from .views import TodosAPIView, TodoAPIView, TodoDoneAPIView

urlpatterns = [
    path('', TodosAPIView.as_view()),
    path('<int:id>/', TodoAPIView.as_view()),
    path('done/', TodoDoneAPIView.as_view()),
]
