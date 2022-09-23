# Generated by Django 3.2.8 on 2021-11-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_battallion_two_on_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battallion_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('nin', models.CharField(max_length=32)),
                ('ipps', models.CharField(max_length=32)),
                ('file_number', models.CharField(max_length=32, unique=True)),
                ('battallion', models.CharField(max_length=32)),
                ('account_number', models.CharField(blank=True, max_length=32, null=True)),
                ('contact', models.CharField(blank=True, max_length=32, null=True)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=32)),
                ('rank', models.CharField(choices=[('AIGP', 'AIGP'), ('SCP', 'SCP'), ('CP', 'CP'), ('ACP', 'ACP'), ('SSP', 'SSP'), ('SP', 'SP'), ('ASP', 'ASP'), ('IP', 'IP'), ('AIP', 'AIP'), ('SGT', 'SGT'), ('CPL', 'CPL'), ('PC', 'PC'), ('SPC', 'SPC')], max_length=32)),
                ('education_level', models.CharField(choices=[('PLE', 'PLE'), ('UCE', 'UCE'), ('UACE', 'UACE'), ('Diploma', 'DIPLOMA'), ('Bachelors', 'BACHELORS'), ('Masters', 'MASTERS'), ('Doctorate', 'DOCTORATE(PhD)'), ('Other', 'OTHER')], max_length=32)),
                ('other_education_level', models.CharField(blank=True, max_length=32, null=True)),
                ('bank', models.CharField(blank=True, max_length=32, null=True)),
                ('branch', models.CharField(blank=True, max_length=32, null=True)),
                ('title', models.CharField(choices=[('Commandant', 'Commandant'), ('Deputy commandant', 'Deputy commandant'), ('Staff officer', 'Staff officer'), ('Head of operations', 'Head of operations'), ('Head of armoury', 'Head of armoury'), ('Supervisor', 'Supervisor'), ('In Charge', 'In Charge'), ('2nd In Charge', '2nd In Charge'), ('Driver', 'Driver')], max_length=32)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Absent', 'Absent(AWOL)'), ('Transfered', 'Transfered'), ('Sick', 'Sick'), ('Dead', 'Dead'), ('Suspended', 'Suspended'), ('Dismissed', 'Dismissed'), ('In court', 'In court'), ('Deserted', 'Deserted'), ('On course', 'On course'), ('On mission', 'On mission')], max_length=32)),
                ('shift', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Long night', 'Long night'), ('None', 'None(not applicable)')], max_length=32)),
                ('date_of_enlistment', models.DateField(blank=True, null=True)),
                ('date_of_transfer', models.DateField(blank=True, null=True)),
                ('date_of_promotion', models.DateField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('armed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=32)),
                ('section', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('on_leave', models.CharField(choices=[('Pass leave', 'Pass leave'), ('Maternity leave', 'Maternity leave'), ('Sick leave', 'Sick leave'), ('Study leave', 'Study leave'), ('Annual leave', 'Annual leave'), ('Not on leave', 'Not on leave')], max_length=32)),
                ('leave_start_date', models.DateField(blank=True, null=True)),
                ('leave_end_date', models.DateField(blank=True, null=True)),
                ('department', models.CharField(choices=[('UN Agencies', 'UN Agencies'), ('Administration', 'Administration'), ('Drivers', 'Drivers')], max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Battallion One',
                'verbose_name_plural': 'Battallion One',
            },
        ),
    ]