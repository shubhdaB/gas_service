from django.contrib import admin
from .models import ServiceRequest, Customer

# Register your models here.
admin.site.register(ServiceRequest)
admin.site.register(Customer)