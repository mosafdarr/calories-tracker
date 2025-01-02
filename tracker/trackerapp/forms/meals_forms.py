from django import forms
from ..models import Meal, MealItem, NutritionGoal, MealPlan

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'date', 'total_calories']

class MealItemForm(forms.ModelForm):
    class Meta:
        model = MealItem
        fields = ['food_item', 'quantity', 'calories']

class NutritionGoalForm(forms.ModelForm):
    class Meta:
        model = NutritionGoal
        fields = ['daily_calorie_goal', 'daily_protein_goal', 'daily_fat_goal', 'daily_carbs_goal']

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['date']
