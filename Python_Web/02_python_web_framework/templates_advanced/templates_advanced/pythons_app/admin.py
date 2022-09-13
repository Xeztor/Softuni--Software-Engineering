from django.contrib import admin
from .models import Python


@admin.register(Python)
class AdminPython(admin.ModelAdmin):
    pass
