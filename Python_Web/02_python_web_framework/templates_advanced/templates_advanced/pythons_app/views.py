from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .core.decorators import only_allow_groups
from .forms import PythonCreateForm
from .models import Python


def index(request):
    pythons = Python.objects.all()
    context = {
        'pythons': pythons,
    }
    return render(request, 'index.html', context)


@login_required()
@only_allow_groups(["User"])
def create(request):
    if request.method == 'POST':
        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PythonCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)
