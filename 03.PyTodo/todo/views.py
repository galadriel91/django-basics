from django.shortcuts import render
from .models import Todo

# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    context={
        'todos':todos
    }
    return render(request, 'todo/todo_list.html', context)

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    context={
        'todo':todo
    }
    return render(request, 'todo/todo_detail.html', context)