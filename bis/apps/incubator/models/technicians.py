"""
Technician Model
"""

# Models
from django.db import models
from ...accounts.models.persons import Person
from ..models.technicianspeciality import TechnicianSpeciality


class Technician(Person):
    TECHINICAN_TYPE_CHOICES = [
        ('CO', 'Coordinador'),
        ('C', 'Consultor'),
        ('M', 'Mentor'),
        ('-', 'Otro'),
    ]
    technician_type = models.CharField(null=True, blank=True, choices=TECHINICAN_TYPE_CHOICES,  max_length=2)
    technician_speciality = models.ForeignKey(TechnicianSpeciality, null=True, blank=True, on_delete=models.SET_NULL)
    company = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return '{0} · {1} {2}'.format(self.identification_number, self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Technician'
        ordering = ['-created_at', '-id']
