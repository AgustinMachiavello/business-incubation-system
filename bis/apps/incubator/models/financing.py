"""
Financing model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin

# Date and time
from django.utils import timezone
from .projects import Project

# Datetime
import datetime

class Financing(TimeStampMixin, models.Model):
    TYPE_CHOICES = [
        ('AE', 'ANDE'),
        ('A1', 'ANII'),
        ('A2', 'ANII Segundo Financiamiento'),
        ('-', 'Otros'),
    ]
    id = models.AutoField(primary_key=True)
    code = models.CharField(null=False, blank=False, max_length=100)
    code_type = models.CharField(null=False, blank=False, max_length=3, choices=TYPE_CHOICES)
    started_on_date = models.DateField(null=False, blank=False)
    finished_on_date = models.DateField(null=False, blank=False)

    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='financing_project')

    def __str__(self):
        return '#{0} · {1} ({2})'.format(self.code, self.project.name, self.code_type)
    
    class Meta:
        verbose_name = 'Financing Code'
        ordering = ['-created_at', '-id']
