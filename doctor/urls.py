from django.urls import path

from . import views

app_name = "doctor"

urlpatterns = [
    path('appointments/', views.appointments, name="appointments"),
    path('prescription/', views.prescription, name="prescription"),
]
