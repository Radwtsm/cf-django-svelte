from enum import unique
from random import choices
from django.db import models
from django.core.validators import MinLengthValidator
import pandas as pd

from django.utils.translation import gettext_lazy as _


class DatiPersona(models.Model):

    FEMMINA = 'F'
    MASCHIO = 'M'

    SESSO = [
        (FEMMINA, 'Femmina'),
        (MASCHIO, 'Maschio'),

    ]

    surname = models.CharField(max_length=200, validators=[
        MinLengthValidator(1)], blank=False)
    name = models.CharField(max_length=200, validators=[
        MinLengthValidator(1)], blank=False)
    sex = models.CharField(max_length=1, choices=SESSO)
    birthdate = models.DateField(
        auto_now=False, auto_now_add=False, blank=False)
    birthplace = models.CharField(max_length=200, blank=False)
    codice_fiscale = models.CharField(max_length=16, validators=[
                                      MinLengthValidator(16)], unique=True, blank=True)

    def __str__(self):
        return f"ID:{self.id},{self.name},{self.surname},{self.sex},{self.codice_fiscale}"
