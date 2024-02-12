from django.contrib import admin
from django.urls import path
from .views import HabitacionList,HabitacionDetail,ReservaDetail,ReservaList,RegisterView,LoginView

urlpatterns = [
    path('habitacion/',HabitacionList.as_view()),
    path('habitacion/<int:pk>/',HabitacionDetail.as_view()),
    path('reserva/',ReservaList.as_view()),
    path('reserva/<int:pk>/',ReservaDetail.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
