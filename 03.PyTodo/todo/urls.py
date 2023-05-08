from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('add/', views.todo_add, name='todo_add'),
    path('<int:pk>/edit', views.todo_edit, name='todo_edit'),
    path('done/', views.done_list, name='done_list'),
]
