from django.db import models


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'
    type = models.CharField(
        max_length=6,
        choices=[
            (TYPE_CHOICE_DOG, 'Dog'),
            (TYPE_CHOICE_CAT, 'Cat'),
            (TYPE_CHOICE_PARROT, 'Parrot'),
        ],
    )

    name = models.CharField(
        max_length=6,
    )
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images', null=True)


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
