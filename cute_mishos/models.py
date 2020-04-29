"""Cute mishos app models"""

from django.db import models


class CuteMisho(models.Model):
    """Creates a new misho with a GIF URL"""
    name = models.CharField('nombre', max_length=70)
    message = models.CharField('mensaje', max_length=200)

    def __str__(self):
        """Returns string representation of misho"""
        return self.name

    def get_image_url(self):
        """Retrieves full image URL"""
        return f'https://cataas.com/cat/cute/says/{self.message}'
