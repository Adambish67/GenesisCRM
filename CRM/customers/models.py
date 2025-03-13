from django.db import models

# Create your models here.
from django.db import models

class Appointment(models.Model):
    DETAIL_TYPE_CHOICES = [
        ('mobile', 'Mobile'),
        ('shop', 'Shop'),
    ]

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    detail_type = models.CharField(max_length=6, choices=DETAIL_TYPE_CHOICES)
    appointment_date = models.DateTimeField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    customer_request = models.TextField(blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer} - {self.appointment_date} ({self.detail_type})"



from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
