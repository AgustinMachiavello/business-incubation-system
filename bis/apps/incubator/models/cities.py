"""
City model
"""

# Models
from django.db import models
from .provinces import Province

class City(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        ordering = ['-id']
