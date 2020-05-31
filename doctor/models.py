from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length = 20)
    mobile = models.IntegerField()
    specialization = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Appointments(models.Model):
    date = models.DateField(blank=True, null= True)
    time = models.TimeField(blank=True, null= True)
    doc_list = (("Doc1", "Doc1"), ("Doc2", "Doc2"), ("Doc3", "Doc3"),)
    consulting_doc = models.CharField(max_length=15, choices=doc_list, default="Doc1")
    status_choices = (("Active", "Active"), ("Pending", "Pending"), ("Completed", "Completed"),)
    status = models.CharField(max_length=10, choices=status_choices, default="Active")

    def __str__(self):
        return self.consulting_doc+" -- "+self.status

class Prescription(models.Model):
    date = models.DateField(blank=True, null=True)
    symptoms = models.CharField(max_length=20, blank=True, null=True)
    prescription = models.CharField(max_length=30, blank=True, null=True)
    patient_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.symptoms+" -- "+self.prescription+" -- "+self.patient_name
