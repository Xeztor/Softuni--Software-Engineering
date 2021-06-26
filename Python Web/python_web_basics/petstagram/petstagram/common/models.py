from django.db import models

from petstagram.pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet)
    comment = models.TextField()
