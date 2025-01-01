# trackerapp/models/user_models.py

from django.db import models
from django.contrib.auth.models import User
from .base_models import BaseModel

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)  # in kilograms
    height = models.FloatField(null=True, blank=True)  # in centimeters
    daily_calorie_goal = models.IntegerField(null=True, blank=True)
