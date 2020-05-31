# Generated by Django 3.0.5 on 2020-05-30 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20200529_1045'),
        ('patient', '0005_auto_20200529_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medical_history',
            name='date2',
        ),
        migrations.AddField(
            model_name='medical_history',
            name='date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription_date', to='doctor.Doctor'),
        ),
        migrations.AddField(
            model_name='medical_history',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription', to='doctor.Doctor'),
        ),
        migrations.AddField(
            model_name='medical_history',
            name='symptoms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='symptoms', to='doctor.Doctor'),
        ),
    ]
