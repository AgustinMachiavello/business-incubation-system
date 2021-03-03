"""
Custom user model
"""

# Base User model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from .persons import Person

# Models
from django.db import models

class User(Person, AbstractUser):
    is_verified = models.BooleanField(default=True, help_text='Set to true when the user have verified its email address.')
    is_staff = models.BooleanField(default=True, help_text='Set to true for accessing the administration panel')
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'identification_number']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
