from django.contrib import admin
from django.urls import path
from .views import HabitacionList,HabitacionDetail

urlpatterns = [
    path('habitacion/',HabitacionList.as_view()),
    path('habitacion/<int:pk>',HabitacionDetail.as_view()),
]
