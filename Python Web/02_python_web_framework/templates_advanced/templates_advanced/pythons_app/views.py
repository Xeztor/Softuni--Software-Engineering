from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


def index(request):
    pythons = Python.objects.all()
    context = {
        'pythons': pythons,
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
    else:
        form = PythonCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)
