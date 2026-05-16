from django.contrib import admin
from .models import Booking, Menu # Import your models

# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)