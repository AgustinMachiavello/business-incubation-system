"""
Interviews model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from .stages import Stage
from .technicians import Technician

# Date and time
from django.utils import timezone

# Datetime
import datetime

class Interview(TimeStampMixin, models.Model):
    INTERVIEW_TYPE_CHOICES = [
        ('EP', 'Entrevista de Postulación'),
        ('SG', 'Seguimiento'),
        ('CA', 'Capacitación'),
        ('SN', 'Taller de Sensibilización'),        
        ('CO', 'Consultoría'),
        ('ME', 'Mentoría'),        
    ]
    INTERVIEW_MODALITY_CHOICES = [
        ('P', 'Presencial'),
        ('O', 'Online'),
    ]
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=True, auto_now=False, auto_now_add=False)
    end_time = models.TimeField(null=True, auto_now=False, auto_now_add=False)
    hours = models.PositiveIntegerField(null=False, blank=False, default=0)
    interview_type = models.CharField(null=False, blank=False, max_length=2, choices=INTERVIEW_TYPE_CHOICES)
    comments = models.TextField()
    modality = models.CharField(null=False, blank=False, max_length=1, choices=INTERVIEW_MODALITY_CHOICES)
    
    stage = models.ForeignKey(Stage, null=False, blank=False, on_delete=models.PROTECT, related_name='interview_stage')
    technicians = models.ManyToManyField(Technician, related_name='interview_technicians')

    def __str__(self):
        return '#{0} · {1} ({2})'.format(self.id, self.stage.project.name, self.get_interview_type_display())

    @property
    def get_time_spent(self):
        # Returns all the time spent for this interview (in hours)
        date = datetime.date(1, 1, 1)
        start = datetime.datetime.combine(date, self.start_time)
        end = datetime.datetime.combine(date, self.end_time)
        difference = ((end - start).total_seconds() / 60**2) # Convert to hours
        return difference

    def save(self, *args, **kwargs):
        self.stage.project.save() # save to update proejct time spent field
        super(Interview, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Interview'
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'stage'], name="const_project_interview_stage")
        ]
        ordering = ['-created_at', '-id']

