"""
Inscription Model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from ..models import City, Province


class Inscription(TimeStampMixin, models.Model):
    SEX_CHOICES = [
        ('N/A', 'No Aplica'),
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    email = models.CharField(null=False, blank=False, max_length=80)
    phone_number = models.CharField(null=False, blank=False, max_length=50)
    sex = models.CharField(null=False, blank=False, choices=SEX_CHOICES, default='N/A', max_length=3)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, null=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='inscription_city')
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    assisted = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return '#{0} · {1}'.format(self.id, self.email)
    
    class Meta:
        verbose_name = 'Inscription'
        ordering = ['-created_at', '-id']
