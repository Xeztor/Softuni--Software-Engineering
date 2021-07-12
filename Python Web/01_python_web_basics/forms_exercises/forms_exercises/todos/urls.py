from django.urls import path

from forms_exercises.todos.views import index, create_todo, edit_todo, delete_todo, do_todo, restart_todo_state

urlpatterns = [
    path('', index, name='index'),
    path('create', create_todo, name='create todo'),
    path('edit/<int:pk>', edit_todo, name='edit todo'),
    path('delete/<int:pk>', delete_todo, name='delete todo'),
    path('do_todo/<int:pk>', do_todo, name='check todo'),
    path('restart todo/<int:pk>', restart_todo_state, name='restart todo'),
]