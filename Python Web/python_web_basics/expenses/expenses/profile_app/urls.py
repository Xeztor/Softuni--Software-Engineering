from django.urls import path

from expenses.profile_app.views import edit_profile, delete_profile, create_profile, profile_details

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('create/', create_profile, name='create profile'),
    path('edit/', edit_profile, name='edit profile'),
    path('delete/', delete_profile, name='delete profile'),
]
