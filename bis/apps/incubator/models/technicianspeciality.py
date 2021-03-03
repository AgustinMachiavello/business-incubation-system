"""
Technician Speciality Model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin


class TechnicianSpeciality(TimeStampMixin, models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technician speciality'
        ordering = ['-created_at', '-id']
