# Generated by Django 5.1.2 on 2024-10-11 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_type', models.CharField(choices=[('mobile', 'Mobile'), ('shop', 'Shop')], max_length=6)),
                ('appointment_date', models.DateTimeField()),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('customer_request', models.TextField(blank=True, null=True)),
                ('internal_notes', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]
