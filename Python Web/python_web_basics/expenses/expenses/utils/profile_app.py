from expenses.expenses.models import Expense
from expenses.profile_app.models import Profile


def get_profile():
    profile = Profile.objects.first()
    return profile


def profile_budget_left():
    profile = Profile.objects.first()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum([expense.price for expense in expenses])

    return budget_left
