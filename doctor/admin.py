from django.contrib import admin

from .models import Appointments, Prescription

# Register your models here.
admin.site.register(Appointments)
admin.site.register(Prescription)
