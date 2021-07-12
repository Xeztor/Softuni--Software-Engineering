from django import forms

from expenses.expenses.models import Expense
from expenses.utils.mixins.BootstrapMixins import DisableFormMixin


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class CreateExpenseForm(ExpenseForm):
    pass


class EditExpenseForm(ExpenseForm):
    pass


class DeleteExpenseForm(DisableFormMixin, ExpenseForm):
    pass
