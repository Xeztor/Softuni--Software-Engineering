from django.shortcuts import render, redirect

from expenses.profile_app.forms import RegisterForm
from expenses.expenses.models import Expense
from expenses.profile_app.forms import EditProfileForm
from expenses.utils.profile_app import get_profile, profile_budget_left


def create_profile(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'form': form
        }
    else:
        context = {
            'form': RegisterForm()
        }

    return render(req, 'profile_app/home-no-profile.html', context)


def profile_details(req):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    profile.budget_left = profile_budget_left()
    context = {
        'profile': profile,
    }
    return render(req, 'profile_app/profile.html', context)


def edit_profile(req):
    profile = get_profile()
    if req.method == "POST":
        form = EditProfileForm(req.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(req, 'profile_app/profile-edit.html', context)


def delete_profile(req):
    profile = get_profile()
    if req.method == "POST":
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home')

    return render(req, 'profile_app/profile-delete.html')

