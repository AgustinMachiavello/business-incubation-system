"""
Postulation page info
"""

# Models
from .singleton import SingletonModel

# Ck Editor
from ckeditor.fields import RichTextField

class SiteSettings(SingletonModel):
    postulation_page_title = RichTextField(null=True, blank=True)
    postulation_page_description = RichTextField(null=True, blank=True)
    postulation_page_info = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return 'Configuración del sitio'.format(self.id)
