from django.contrib import admin

from .models import Your_Appointments, Invoices_Payemnts, Profile, Medical_History

# Register your models here.
admin.site.register(Your_Appointments)
admin.site.register(Invoices_Payemnts)
admin.site.register(Profile)
admin.site.register(Medical_History)