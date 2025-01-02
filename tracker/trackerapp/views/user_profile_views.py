from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import UserProfile, NutritionGoal
from ..forms.user_forms import UserProfileForm
from ..forms.meals_forms import NutritionGoalForm

@login_required
def edit_profile(request):
    if not UserProfile.objects.filter(user=request.user).exists():
        UserProfile.objects.create(user=request.user)
    profile = UserProfile.objects.get(user=request.user)

    if not NutritionGoal.objects.filter(user=request.user).exists():
        NutritionGoal.objects.create(user=request.user)
    nutrition_goal = NutritionGoal.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=profile)
        nutrition_goal_form = NutritionGoalForm(request.POST, instance=nutrition_goal)

        if user_form.is_valid() and nutrition_goal_form.is_valid():
            user_form.save()
            nutrition_goal_form.save()
            messages.success(request, 'Profile updated successfully!')

            return redirect('trackerapp:view_profile')
    else:
        user_form = UserProfileForm(instance=profile)
        nutrition_goal_form = NutritionGoalForm(instance=nutrition_goal)

    return render(
        request,
        'trackerapp/profile.html',
        {'user_form': user_form, 'nutrition_goal_form': nutrition_goal_form}
    )

def view_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'trackerapp/profile.html', {'profile': profile})
