from django.shortcuts import render, redirect

from forms_exercises.todos.forms import TodoForm, EditTodoForm
from forms_exercises.todos.models import Todo


def index(req):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(req, 'todo_app/index.html', context=context)


def create_todo(req):
    if req.method == "POST":
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()

    context = {
        'form': form,
    }

    return render(req, 'todo_app/create.html', context=context)


def edit_todo(req, pk):
    todo = Todo.objects.get(pk=pk)

    if req.method == "GET":
        form = EditTodoForm(instance=todo)
    else:
        form = EditTodoForm(req.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(req, 'todo_app/edit.html', context=context)


def delete_todo(_, pk):
    todo = Todo.objects.get(pk=pk)

    todo.delete()
    return redirect('index')


def do_todo(_, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.state is False:
        todo.state = True
        todo.save()

    return redirect('index')


def restart_todo_state(_, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.state is True:
        todo.state = False
        todo.save()

    return redirect('index')
