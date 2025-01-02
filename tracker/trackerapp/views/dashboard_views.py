from django.shortcuts import render, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from ..models import Meal, NutritionGoal


@login_required
def dashboard(request):
    user = request.user
    today = timezone.now().date()
    meals_today = Meal.objects.filter(user=user, date=today)
    total_calories_today = sum(meal.total_calories for meal in meals_today)

    try:
        nutrition_goal = NutritionGoal.objects.get(user=user)
    except NutritionGoal.DoesNotExist:
        nutrition_goal = None
    

    context = {
        'meals_today': meals_today,
        'total_calories_today': total_calories_today,
        'nutrition_goal': nutrition_goal,
    }

    # return render(request, 'dashboard.html', context)
    return HttpResponse(context)
