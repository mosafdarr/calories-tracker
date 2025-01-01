# trackerapp/models/food_models.py

from django.db import models
from .base_models import BaseModel

class FoodItem(BaseModel):
    name = models.CharField(max_length=255)
    calories = models.FloatField()  # calories per serving
    protein = models.FloatField(null=True, blank=True)  # grams of protein per serving
    fat = models.FloatField(null=True, blank=True)  # grams of fat per serving
    carbs = models.FloatField(null=True, blank=True)  # grams of carbohydrates per serving
    serving_size = models.CharField(max_length=100, null=True, blank=True)  # description of serving size, e.g., "1 cup", "100g"
