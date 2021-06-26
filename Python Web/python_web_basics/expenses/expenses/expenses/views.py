from django.shortcuts import render, redirect

from expenses.expenses.forms import CreateExpenseForm, EditExpenseForm, DeleteExpenseForm
from expenses.expenses.models import Expense
from expenses.utils.profile_app import get_profile, profile_budget_left


def home(req):
    profile = get_profile()

    if profile is None:
        return redirect('create profile')

    expenses = Expense.objects.all()
    profile.budget_left = profile_budget_left()
    context = {
        'profile': profile,
        'expenses': expenses,
    }

    return render(req, 'home-with-profile.html', context)


def create_expense(req):
    if req.method == "POST":
        form = CreateExpenseForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form,
    }
    return render(req, 'expense-create.html', context)


def edit_expense(req, pk):
    expense = Expense.objects.get(pk=pk)
    if req.method == "POST":
        form = EditExpenseForm(req.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,
    }
    return render(req, 'expense-edit.html', context)


def delete_expense(req, pk):
    expense = Expense.objects.get(pk=pk)
    if req.method == "POST":
        expense.delete()
        return redirect('home')

    form = DeleteExpenseForm(instance=expense)
    context = {
        'expense': expense,
        'form': form,
    }

    return render(req, 'expense-delete.html', context)
