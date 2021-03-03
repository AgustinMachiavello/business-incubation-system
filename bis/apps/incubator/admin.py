from django.contrib import admin

# Models
from .models import Province
from .models import City
from .models import Activity
from .models import BusinessArea
from .models import Broadcast
from .models import Entrepreneur
from .models import File
from .models import Interview
from .models import Postulation
from .models import Project
from .models import Stage
from .models import Technician
from .models import Financing
from .models import Inscription
from .models import TechnicianSpeciality
from .models import SingletonModel
from .models import SiteSettings

# Register your models here.
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Activity)
admin.site.register(BusinessArea)
admin.site.register(Broadcast)
admin.site.register(Entrepreneur)
admin.site.register(File)
admin.site.register(Interview)
admin.site.register(Postulation)
admin.site.register(Project)
admin.site.register(Stage)
admin.site.register(Technician)
admin.site.register(Financing)
admin.site.register(Inscription)
admin.site.register(TechnicianSpeciality)
admin.site.register(SiteSettings)