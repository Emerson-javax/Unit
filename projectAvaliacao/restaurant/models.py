from django.db import models

# Create your models here.


class Restaurants(models.Model):
    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False,
    )

    cidade = models.CharField(
        max_length=14,
        null=False,
        blank=False,
    )

    senha = models.CharField(
        max_length=8,
        null=False,
        blank=False,
    )
