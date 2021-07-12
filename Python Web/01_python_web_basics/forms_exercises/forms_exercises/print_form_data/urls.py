from django.urls import path

from forms_exercises.print_form_data.views import form

urlpatterns = [
    path('', form, name='send data'),
]
