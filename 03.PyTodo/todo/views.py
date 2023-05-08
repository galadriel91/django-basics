from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

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

def todo_add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    context={
        'form':form
    }
    return render(request, 'todo/todo_add.html', context)