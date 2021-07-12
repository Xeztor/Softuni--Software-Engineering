from django.urls import path

from notes.profile_app.views import profile_details, delete_profile

urlpatterns = [
    path('profile/', profile_details, name='profile details'),
    path('profile_delete/', delete_profile, name='profile delete'),
]
