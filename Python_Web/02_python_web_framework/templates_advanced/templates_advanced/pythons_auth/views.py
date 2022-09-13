from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from templates_advanced.pythons_auth.forms import SignInForm, RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignInForm()

    context = {
        'form': form,
    }
    return render(request, 'auth/sign-in.html', context)


def sign_out(request):
    logout(request)
    return redirect('index')
