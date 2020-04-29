"""Mishos URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('cute_mishos.urls', 'cute_mishos'), namespace='cute_mishos')),
]
