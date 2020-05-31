# Generated by Django 3.0.5 on 2020-05-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('specialization', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='date_time',
        ),
        migrations.AddField(
            model_name='appointments',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]