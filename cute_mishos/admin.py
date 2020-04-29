"""Cute mishos app admin site"""

from django.contrib import admin

from .models import CuteMisho


admin.site.register(CuteMisho)
