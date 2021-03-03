"""
Person Model
"""

# Models
from django.db import models

# Date and time
from django.utils import timezone

# Validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_identification_number(value):
    if not (value and isinstance(value, int) and (0 <= value) and (value <= 9999999999)):
        raise ValidationError(
            _('%(value)s no es una cédula válida'),
            params={'value': value},
        )

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    identification_number = models.PositiveIntegerField('cédula', unique=True, blank=False, validators=[validate_identification_number])
    first_name = models.CharField(null=False, blank=False, max_length=50)
    last_name = models.CharField(null=False, blank=False, max_length=100)    
    phone_number = models.CharField(null=False, blank=False, max_length=50)    
    email = models.EmailField('correo', null=False, blank=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'persona'
        ordering = ['-id']
