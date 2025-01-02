from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from ..forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('trackerapp:index')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('trackerapp:index')
