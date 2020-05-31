from django.shortcuts import render
from .models import Appointments, Prescription
# Create your views here.

def appointments(request):
    data1 = Appointments.objects.all()
    context = {
        'data':data1,
    }
    return render(request, 'appointments_details.html', context)

def prescription(request):
    data2 = Prescription.objects.all()
    context = {
        'data':data2,
    }
    return render(request, 'prescription_details.html', context)
