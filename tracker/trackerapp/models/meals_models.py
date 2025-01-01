# trackerapp/models/meals_models.py

from django.db import models
from django.contrib.auth.models import User
from .base_models import BaseModel
from .food_models import FoodItem

class Meal(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g., "Breakfast", "Lunch", "Dinner"
    date = models.DateField()  # Date of the meal
    total_calories = models.FloatField(default=0.0)  # Total calories in the meal


class MealItem(BaseModel):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.FloatField()  # How many servings the user consumed
    calories = models.FloatField()  # Total calories for this food item (based on quantity)


class NutritionGoal(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_calorie_goal = models.IntegerField(default=2000)
    daily_protein_goal = models.FloatField(null=True, blank=True)  # Grams of protein
    daily_fat_goal = models.FloatField(null=True, blank=True)  # Grams of fat
    daily_carbs_goal = models.FloatField(null=True, blank=True)  # Grams of carbs


class MealPlan(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()  # The date for which the meal plan is created


class MealPlanItem(BaseModel):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, related_name='plan_items')
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.FloatField()  # Planned servings
    calories = models.FloatField()  # Planned total calories for this food item
