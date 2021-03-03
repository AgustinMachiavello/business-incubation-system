"""
Stage model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from ..models.projects import Project

# Date and time
from django.utils import timezone


class Stage(TimeStampMixin, models.Model):
    STAGE_TYPE_CHOICES = [
        ('EP', 'En Postulación'),
        ('EV', 'Evaluación Incubadora/Capital Semilla'),
        ('PI', 'Pre-Incubación'),
        ('IN', 'Incubación'),
        ('PO', 'Post-Incubación'),
    ]
    stage_type = models.CharField(null=False, blank=False, choices=STAGE_TYPE_CHOICES, max_length=2)
    description = models.CharField(null=False, blank=False, max_length=1000)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    # time_spent_interviews = models.FloatField(null=True, blank=True, editable=False)
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stage_project')

    @property
    def get_time_spent(self):
        # Returns all the time spent on interviews for this stage (in hours)
        hours = 0
        for i in self.interview_stage.all():
            hours += i.get_time_spent
        return hours

    def __str__(self):
        return '#{0} · {1} · {2}'.format(self.id, self.project.name, self.get_stage_type_display())
    
    def save(self, *args, **kwargs):
          # self.time_spent_interviews = self.get_time_spent
          super(Stage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Stage'
        constraints = [
            models.UniqueConstraint(
                fields=['project', 'stage_type'], name="const_project_stage")
        ]
        ordering = ['-created_at', '-id']
