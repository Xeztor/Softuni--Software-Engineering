from django.contrib import admin

from petstagram.pets.models import Pet, Like


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
