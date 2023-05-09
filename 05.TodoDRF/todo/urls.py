from django.urls import path
from .views import TodosAPIView

urlpatterns = [
    path('' , TodosAPIView.as_view())
]
