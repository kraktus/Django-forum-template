from django.contrib import admin

# Register your models here.
from .models import RegisterRequest

admin.site.register(RegisterRequest)