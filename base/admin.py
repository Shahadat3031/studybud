from django.contrib import admin

# Register your models here.
from .models import Room

# Registering the Room model with the admin site
admin.site.register(Room)