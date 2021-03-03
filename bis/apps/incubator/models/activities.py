"""
Activities Model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from .inscriptions import Inscription
from ...accounts.models.users import User
import datetime

# Slug
from slugify import slugify

# Random strings and numbers
import random
import string

# Django
from django.urls import reverse
from django.contrib.sites.models import Site

# Ck Editor
from ckeditor.fields import RichTextField


class Activity(TimeStampMixin, models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('SE', 'Sensibilización'),
        ('PI', 'Pre-Incubación'),
        ('IN', 'Incubación'),
        ('PO', 'Post-Incubación'),
    ]
    title = models.CharField(null=False, blank=False, max_length=50)
    date = models.DateField(null=False, blank=False)
    activity_type = models.CharField(max_length=2, choices=ACTIVITY_TYPE_CHOICES)
    description = RichTextField(null=True, blank=True)
    inscription_deadline = models.DateField(null=True, blank=True)
    inscription_time_message = models.TextField(null=True, blank=True)
    attendance_limit = models.PositiveIntegerField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    inscription_link = models.SlugField(null=True, blank=True, unique=True)

    #responsable
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    inscriptions = models.ManyToManyField(Inscription, related_name='activity_inscriptions')

    def __str__(self):
        return "{0}".format(self.title)

    def save(self, *args, **kwargs):
        if not self.inscription_link:
            letters_and_digits = string.ascii_letters + string.digits
            result_str = ''.join(random.choice(letters_and_digits) for i in range(32))
            result_str = slugify(result_str)
            self.inscription_link = result_str
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Activity'
        ordering = ['-created_at', '-id']

