from django.contrib import admin
from django_use_email_as_username.admin import BaseUserAdmin

from .models import User

# Registering User model
admin.site.register(User, BaseUserAdmin)
