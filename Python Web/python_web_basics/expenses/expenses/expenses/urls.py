from django.urls import path

from expenses.expenses.views import home, edit_expense, create_expense, delete_expense

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),
]
