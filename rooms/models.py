from django.db import models
# from django_countries.fields import CountryField
from core.models import models as core_models


# Create your models here.

class Room(core_models.TimeStampedModel):

    """Room model definition"""
    name = models.CharField(max_length=140)
    description = models.TextField()
    # country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    guests = models.IntegerField(help_text="How many people will be a staying?")
    price = models.IntegerField()
    beds = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms")
