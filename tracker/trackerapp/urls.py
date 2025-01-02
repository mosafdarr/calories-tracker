from django.urls import path
from . import views

app_name = 'trackerapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.view_profile, name='view_profile'),
    # path('add/', views.add_food, name='add_food'),
    # path('delete/<int:food_id>/', views.delete_food, name='delete_food'),
    # path('update/<int:food_id>/', views.update_food, name='update_food'),
]
