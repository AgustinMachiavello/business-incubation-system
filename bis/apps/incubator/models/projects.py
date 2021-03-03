"""
Project model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from .businessareas import BusinessArea
from .entrepreneurs import Entrepreneur
from .postulations import Postulation
from ...accounts.models.users import User

# Date and time
from django.utils import timezone

# Validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_rut(value):
    if not (value and isinstance(value, int) and (0 <= value) and (value <= 99999999999999)):
        raise ValidationError(
            _('%(value)s no es un RUT válido'),
            params={'value': value},
        )


class Project(TimeStampMixin, models.Model):
    STATUS_CHOICES = [
        ('P', 'En progreso'),
        ('G', 'Graduado'),
        ('E', 'Egresado'),
    ]
    GENERAL_STAGE_CHOICES = [
        ('-', '---'),
        ('DE', 'Desarrollo del Producto o Servicio / Puesta en Marcha'),
        ('CO', 'Comercialización Temprana'),
        ('CN', 'Consolidación Comercial e Internacionalización'),
    ]
    name = models.CharField(null=False, blank=False, max_length=100)
    social_reason = models.CharField(null=False, blank=False, max_length=100)
    rut = models.BigIntegerField(unique=True, blank=False, validators=[validate_rut])
    description = models.TextField(null=True, blank=True)
    status = models.CharField(null=False, blank=False, max_length=1, choices=STATUS_CHOICES, default='-')
    general_stage = models.CharField(null=False, blank=False, max_length=2, choices=GENERAL_STAGE_CHOICES, default='-')
    
    business_area = models.ForeignKey(BusinessArea, on_delete=models.SET_NULL, null=True, related_name='project_business_area')    
    postulation = models.ForeignKey(Postulation, on_delete=models.SET_NULL, null=True)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    entrepreneurs = models.ManyToManyField(Entrepreneur, related_name='project_entrepreneurs')

    time_spent = models.FloatField(null=True, blank=True, editable=False)

    def __str__(self):
        return '#{0} · {1} - {2}'.format(self.id, self.rut, self.name)

    @property
    def get_time_spent(self):
        # Returns all the time spent on interviews for this project (in hours)
        hours = 0
        for i in self.stage_project.all():
            hours += i.get_time_spent
        return hours

    def save(self, *args, **kwargs):
          self.time_spent = self.get_time_spent
          super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Proyecto'
        ordering = ['-created_at', '-id']
