"""
Business area model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin

# Date and time
from django.utils import timezone

class BusinessArea(TimeStampMixin, models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at', '-id']
