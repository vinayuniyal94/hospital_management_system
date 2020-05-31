from django.urls import path

from . import views

app_name = "patient"

urlpatterns = [
    path('yourAppointments/', views.yourAppointments, name="yourAppointments"),
    path('invoicePrescription/', views.invoicePrescription, name="invoicePrescription"),
    path('medicalHistory/', views.medicalHistory, name="medicalHistory"),
    path('profile/', views.profile, name="profile"),
]
