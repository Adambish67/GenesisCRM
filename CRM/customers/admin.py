from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer

admin.site.register(Customer)

from django.contrib import admin
from .models import Customer, Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'appointment_date', 'detail_type', 'make', 'model')
    search_fields = ('customer__first_name', 'customer__last_name', 'make', 'model')
    list_filter = ('detail_type', 'appointment_date')
    ordering = ('-appointment_date',)
    readonly_fields = ('internal_notes',)


from django.contrib.admin import widgets
from django import forms

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointment_date': widgets.AdminSplitDateTime(),
        }

class AppointmentAdmin(admin.ModelAdmin):
    form = AppointmentForm
    list_display = ('customer', 'appointment_date', 'detail_type', 'make', 'model')
    search_fields = ('customer__first_name', 'customer__last_name', 'make', 'model')
    list_filter = ('detail_type', 'appointment_date')
    ordering = ('-appointment_date',)
    readonly_fields = ('internal_notes',)
