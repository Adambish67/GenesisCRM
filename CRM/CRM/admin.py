from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import admin

class CustomAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        return HttpResponseRedirect(reverse('admin_dashboard'))

admin_site = CustomAdminSite(name='myadmin')
admin_site.register(Customer)
admin_site.register(Appointment)

