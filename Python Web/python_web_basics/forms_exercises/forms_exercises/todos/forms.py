from django.forms import models

from forms_exercises.todos.models import Todo


class TodoForm(models.ModelForm):
    class Meta:
        model = Todo
        exclude = ('state',)


class EditTodoForm(models.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

    # def clean_state(self):
    #     if self.cleaned_data['state'] == 'on':
    #         return True
    #     return False
