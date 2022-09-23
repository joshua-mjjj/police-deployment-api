# Generated by Django 3.2.8 on 2022-02-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_user_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battallion_five',
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
                ('tin_number', models.CharField(blank=True, max_length=32, null=True)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=32)),
                ('rank', models.CharField(choices=[('AIGP', 'AIGP'), ('SCP', 'SCP'), ('CP', 'CP'), ('ACP', 'ACP'), ('SSP', 'SSP'), ('SP', 'SP'), ('ASP', 'ASP'), ('IP', 'IP'), ('AIP', 'AIP'), ('SGT', 'SGT'), ('CPL', 'CPL'), ('PC', 'PC'), ('SPC', 'SPC')], max_length=32)),
                ('education_level', models.CharField(choices=[('PLE', 'PLE'), ('UCE', 'UCE'), ('UACE', 'UACE'), ('Diploma', 'DIPLOMA'), ('Post Graduate Diploma', 'POST GRADUATE DIPLOMA'), ('Bachelors', 'BACHELORS'), ('Masters', 'MASTERS'), ('Doctorate', 'DOCTORATE(PhD)'), ('Other', 'OTHER')], max_length=32)),
                ('other_education_level', models.CharField(blank=True, max_length=32, null=True)),
                ('bank', models.CharField(blank=True, max_length=32, null=True)),
                ('branch', models.CharField(blank=True, max_length=32, null=True)),
                ('department', models.CharField(choices=[('UCC', 'UCC'), ('EC', 'EC'), ('IRA', 'IRA'), ('URA', 'URA'), ('UNRA', 'UNRA'), ('NPA', 'NPA'), ('ULC', 'ULC'), ('NSSF', 'NSSF'), ('KCCA', 'KCCA'), ('SENIOR CITIZENS', 'SENIOR CITIZENS'), ('JSC', 'JSC')], max_length=150)),
                ('title', models.CharField(choices=[('Commandant', 'Commandant'), ('Deputy commandant', 'Deputy commandant'), ('Staff officer', 'Staff officer'), ('Head of operations', 'Head of operations'), ('Head of armoury', 'Head of armoury'), ('Supervisor', 'Supervisor'), ('In Charge', 'In Charge'), ('2nd In Charge', '2nd In Charge'), ('Driver', 'Driver'), ('N/A', 'N/A')], max_length=32)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Absent', 'Absent(AWOL)'), ('Transfered', 'Transfered'), ('Sick', 'Sick'), ('Dead', 'Dead'), ('Suspended', 'Suspended'), ('Dismissed', 'Dismissed'), ('In court', 'In court'), ('Deserted', 'Deserted'), ('On course', 'On course'), ('On mission', 'On mission'), ('On leave', 'On leave'), ('Interdiction', 'Interdiction'), ('Criminal court', 'Criminal court(remand / bail)'), ('Displinary court', 'Displinary court'), ('Special duty', 'Special duty'), ('On police course', 'On police course'), ('Undeployed', 'Undeployed')], max_length=32)),
                ('shift', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Long night', 'Long night'), ('None', 'None(not applicable)')], max_length=32)),
                ('date_of_enlistment', models.DateField(blank=True, null=True)),
                ('date_of_transfer', models.DateField(blank=True, null=True)),
                ('date_of_promotion', models.DateField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('armed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=32)),
                ('section', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('on_leave', models.CharField(choices=[('Pass leave', 'Pass leave'), ('Maternity leave', 'Maternity leave'), ('Sick leave', 'Sick leave'), ('Study leave', 'Study leave'), ('Annual leave', 'Annual leave'), ('Not on leave', 'Not on leave')], max_length=32)),
                ('notify_leave', models.BooleanField(default=False)),
                ('notify_special_duty', models.BooleanField(default=False)),
                ('special_duty_start_date', models.DateField(blank=True, null=True)),
                ('special_duty_end_date', models.DateField(blank=True, null=True)),
                ('leave_start_date', models.DateField(blank=True, null=True)),
                ('leave_end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Battallion Five',
                'verbose_name_plural': 'Battallion Five',
            },
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='department',
            field=models.CharField(choices=[('Embassy', 'Embassy'), ('Consulate', 'Consulate'), ('High Commission', 'High Commission'), ('Other Diplomats', 'Other Diplomats'), ('Administration', 'Administration')], max_length=32),
        ),
    ]
