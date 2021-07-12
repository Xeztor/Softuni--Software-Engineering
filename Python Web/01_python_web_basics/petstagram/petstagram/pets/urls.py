from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from petstagram.pets.views import create_pet, edit_pet, delete_pet, pet_list, pet_detail, like_pet

urlpatterns = [
    path('', pet_list, name='pets list'),
    path('detail/<int:pk>', pet_detail, name='pet detail'),
    path('like/<int:pk>', like_pet, name='like pet'),
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

