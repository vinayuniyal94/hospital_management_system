from django.db import models

from doctor.models import Doctor


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=16, blank=True, null=True)
    gender = models.CharField(max_length=6)
    age = models.IntegerField()
    address = models.CharField(max_length=20, blank=True, null=True)
    bloodgroup = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name+"--"+self.gender+"--"+self.bloodgroup

class Your_Appointments(models.Model):
    date1 = models.DateField(blank=True, null=True)
    time1 = models.TimeField(blank=True, null = True)
    doc_list = (("Doc1", "Doc1"), ("Doc2", "Doc2"), ("Doc3", "Doc3"),)
    consulting_doc = models.CharField(max_length=15, choices=doc_list, default="Doc1")
    status_choices = (("Active", "Active"), ("Pending", "Pending"), ("Completed", "Completed"),)
    status = models.CharField(max_length=10, choices=status_choices, default="Active")

    def __str__(self):
        return self.consulting_doc+" -- "+self.status


class Invoices_Payemnts(models.Model):
    paid = models.IntegerField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    outstanding = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.date1)+" -- "+str(self.paid)+" -- "+str(self.outstanding)

class Medical_History(models.Model):
    date = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name = 'prescription_date', null=True, blank=True)
    symptoms = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name = 'symptoms', null=True, blank=True)
    prescription = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name = 'prescription', null=True, blank=True)

    def __str__(self):
        return self.symptoms+"--"+self.prescription
