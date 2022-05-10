# Generated by Django 4.0.4 on 2022-05-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatmentinprogress',
            name='start_time',
        ),
        migrations.AddField(
            model_name='treatmentinprogress',
            name='duration',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lifestyle',
            name='water_quality',
            field=models.CharField(choices=[('Mineral water', 'Mineral water'), ('Tap water', 'Tap water'), ('Water from the source', 'Water from the source'), ('River water', 'River water'), ('Potable water', 'Potable water'), ('Well water', 'Well water')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O-', 'O-'), ('O+', 'O+')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='civil_status',
            field=models.CharField(choices=[('SINGLE', 'SINGLE'), ('MARRIED', 'MARRIED'), ('DIVORCED', 'DIVORCED')], max_length=50),
        ),
        migrations.AlterField(
            model_name='virtualpatient',
            name='civil_status',
            field=models.CharField(choices=[('SINGLE', 'SINGLE'), ('MARRIED', 'MARRIED'), ('DIVORCED', 'DIVORCED')], max_length=50),
        ),
    ]
