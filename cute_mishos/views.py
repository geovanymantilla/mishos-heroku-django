"""Cute mishos app views"""

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import CuteMisho


class CuteMishoListView(ListView):
    """Show all mishos"""
    model = CuteMisho
    template_name = 'cute_mishos/list.html'



class CuteMishoCreateView(CreateView):
    """Creates a new misho"""
    model = CuteMisho
    fields = '__all__'
    template_name = 'cute_mishos/create.html'
    success_url = reverse_lazy('cute_mishos:list')

    def form_valid(self, form):
        """Sends a success message"""
        name = form.cleaned_data.get('name')
        messages.success(
            request=self.request,
            message=f'Se ha creado correctamente el misho {name}.'
        )
        return super().form_valid(form)

