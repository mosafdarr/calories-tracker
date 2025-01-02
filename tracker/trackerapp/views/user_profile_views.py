from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import UserProfile
from ..forms.user_forms import UserProfileForm


@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('trackerapp:view_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'trackerapp/profile.html', {'form': form})

def view_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'trackerapp/profile.html', {'profile': profile})
