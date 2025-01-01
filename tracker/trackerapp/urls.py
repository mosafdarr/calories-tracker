from django.urls import path
from . import views

app_name = 'trackerapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    # path('add/', views.add_food, name='add_food'),
    # path('delete/<int:food_id>/', views.delete_food, name='delete_food'),
    # path('update/<int:food_id>/', views.update_food, name='update_food'),
]
