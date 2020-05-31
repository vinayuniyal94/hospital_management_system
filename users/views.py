from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/users/templates/login.html')


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    userType = request.POST.get("userType")
    print(userType)
    user = authenticate(request, username=username, password=password)

    context = {
        "userType":f"{userType}",
    }

    if (userType == "doctor"):
        if user is not None:
            login(request, user)
            return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/users/templates/loginDashboard_doctor.html')
        else:
            return render(request, "/home/vinay/Documents/PROJECT/hospital_managemet_system/users/templates/login.html", {"message": "Invalid Credentials"})

    else:
        if user is not None:
            login(request, user)
            return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/users/templates/loginDashboard_patient.html', context)
        else:
            return render(request, "user/login.html", {"message": "Invalid Credentials"})



def register(request):
    return render(request, '/home/vinay/Documents/PROJECT/hospital_managemet_system/users/templates/register.html')


def logout_view(request):
    logout(request)
    return render(request, "/home/vinay/Documents/PROJECT/hospital_managemet_system/users/templates/login.html")


def home(request):
    return render(request, "/home/vinay/Documents/PROJECT/hospital_managemet_system/users/templates/baseDoctor_loginDasboard.html")
