# Generated by Django 5.0.7 on 2024-07-18 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=500)),
                ('Department', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=500)),
            ],
        ),
    ]
