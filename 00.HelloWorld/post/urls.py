from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_list, name='main_list'),
    path('post/<int:pk>/', views.main_item, name='main_item'),
]
