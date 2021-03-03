"""
Province model
"""

# Models
from django.db import models


class Province(models.Model):
    name = models.CharField(null=False, blank=False, max_length=25)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Province'
        ordering = ['-id']
