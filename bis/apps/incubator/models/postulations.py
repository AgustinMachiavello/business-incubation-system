"""
Postulation model
"""

# Models
from django.db import models
from .timeStampMixin import TimeStampMixin
from .businessareas import BusinessArea
from .entrepreneurs import Entrepreneur
from ..models import City, Province

# Date and time
from django.utils import timezone


class Postulation(TimeStampMixin, models.Model):
    STATUS_CHOICES = [
        ('-', '---'),
        ('P', 'Pre-Seleccionado'),
        ('D', 'Derivado'),
    ]
    PROGRESS_CHOICES = [
        ('IOD', 'Idea o concepto'),
        ('PSD', 'Producto/servicio en desarrollo'),
        ('PLV', 'Prototipo Listo y Validado'),
        ('PCL', 'Producto completo y listo para lanzar al mercado'),
    ]
    name = models.CharField(null=False, blank=False, max_length=50)
    description = models.TextField(null=False, blank=False, help_text="""
    Describe brevemente cuál es el producto/servicio que planteas desarrollar y qué problema ó necesidad de tu cliente resuelves.  Cuéntanos qué tiene de diferente tu producto/servicio respecto a otros que ya se venden en el mercado.
    """)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, null=False)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='postulation_city', help_text="""
    Ingresa el nombre de la ciudad o de su departamento
    """)
    status = models.CharField(null=False, blank=False, max_length=1, choices=STATUS_CHOICES, default='-')
    progress = models.CharField(null=False, blank=False, max_length=3, choices=PROGRESS_CHOICES, default='IOD')
    postulant = models.ForeignKey(Entrepreneur, on_delete=models.PROTECT, null=False, blank=False)
    business_area = models.ForeignKey(BusinessArea, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return '#{0} · {1} - {2} ({3})'.format(self.id, self.postulant, self.name, self.business_area)
    
    class Meta:
        verbose_name = 'Postulation'
        ordering = ['-created_at', '-id']
