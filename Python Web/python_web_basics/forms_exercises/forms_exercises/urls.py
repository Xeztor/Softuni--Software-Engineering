from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('forms_exercises.print_form_data.urls')),
    path('todos_app/', include('forms_exercises.todos.urls')),
]
