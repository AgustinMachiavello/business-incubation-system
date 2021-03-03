"""
Files model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from .projects import Project
from .interviews import Interview
from .stages import Stage
from .entrepreneurs import Entrepreneur

class File(TimeStampMixin, models.Model):
    name = models.CharField(null=False, blank=False, max_length=200)
    file_link = models.URLField(null=False, blank=False, max_length=5000)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.SET_NULL, related_name='file_project')
    interview = models.ForeignKey(Interview, null=True, blank=True, on_delete=models.SET_NULL, related_name='file_interview')
    stage = models.ForeignKey(Stage, null=True, blank=True, on_delete=models.SET_NULL, related_name='file_stage', help_text='')
    entrepreneur = models.ForeignKey(Entrepreneur, null=True, blank=True, on_delete=models.SET_NULL, related_name='file_entrepreneur')
    
    def __str__(self):
        return '#{0} · {1}'.format(self.id, self.name)

    class Meta:
        ordering = ['-created_at', '-id']