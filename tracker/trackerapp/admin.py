from django.contrib import admin

from .models.user_models import UserProfile
from .models.food_models import FoodItem
from .models.meals_models import Meal, MealItem

# Register your models as usual
admin.site.register(UserProfile)
admin.site.register(FoodItem)
admin.site.register(Meal)
admin.site.register(MealItem)
