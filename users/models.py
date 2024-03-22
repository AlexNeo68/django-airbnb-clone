from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )

    LANG_EN = 'en'
    LANG_RU = 'ru'

    LANG_CHOICES = (
        (LANG_EN, 'English'),
        (LANG_RU, 'Russian'),
    )

    CURRENCY_USD = 'USD'
    CURRENCY_RUB = 'RUB'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, 'USD'),
        (CURRENCY_RUB, 'RUB'),
    )

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    language = models.CharField(choices=LANG_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
