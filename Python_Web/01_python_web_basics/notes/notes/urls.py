from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.notes.urls')),
    path('', include('notes.profile_app.urls')),
]
