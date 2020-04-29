"""Cute mishos URL config"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.CuteMishoListView.as_view(), name='list'),
    path('create', views.CuteMishoCreateView.as_view(), name='create'),
]