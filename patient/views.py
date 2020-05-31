from django.shortcuts import render

from .models import Profile, Your_Appointments, Invoices_Payemnts, Medical_History

# Create your views here.

def yourAppointments(request):
    data = Your_Appointments.objects.all()
    context = {
        'data':data,
    }
    return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/patient/templates/yourAppointments.html',context)

def invoicePrescription(request):
    data = Invoices_Payemnts.objects.all()
    context = {
        'data':data,
    }
    return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/patient/templates/invoice_prescription.html',context)

def medicalHistory(request):
    data = Medical_History.objects.all()
    context = {
        "data":data,
    }
    return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/patient/templates/medical_history.html',context)

def profile(request):
    data = Profile.objects.all()
    context = {
        "data":data,
    }
    return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/patient/templates/profile.html',context)
