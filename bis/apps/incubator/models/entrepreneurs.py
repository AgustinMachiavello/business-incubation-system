"""
Entrepreneur model
"""

# Models
from django.db import models
from .cities import City
from ...accounts.models.users import User

# datetime
from datetime import date


class Entrepreneur(User):
    SEX_CHOICES = [
        ('N/A', 'No Aplica'),
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    date_of_birth = models.DateField(null=True, blank=False)
    sex = models.CharField(null=False, blank=False, choices=SEX_CHOICES, default='N/A', max_length=3)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='entrepreneur_city')

    class Meta:
        verbose_name = 'Entrepreneur'
        ordering = ['-created_at', '-id']

    def __str__(self):
        return "{0} · {1} {2}".format(self.identification_number, self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.is_staff = False
        super(Entrepreneur, self).save(*args, **kwargs)