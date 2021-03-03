"""Model forms"""

# Django
from django.forms import ModelForm, Form
from django import forms
# from django.contrib.auth.forms import UserCreationForm avoid this, as it exposes the password modification

# Ajax autocomplete
from ajax_select.fields import AutoCompleteSelectMultipleField, AutoCompleteSelectField

# Models
from ..models import (
    Activity,
    BusinessArea,
    Broadcast,
    Entrepreneur,
    File,
    Interview,
    Postulation,
    Project,
    Stage,
    Technician,
    City,
    Financing,
    Province,
    Inscription,
    TechnicianSpeciality,
    SiteSettings,
)

from ...accounts.models import User

# Validators
from django.core.exceptions import ValidationError

# Ck Editor
from ckeditor.fields import RichTextField


def set_attribute(visible):
    if ('date' in visible.name or visible.name in ['inscription_deadline'] ):
        visible.field.widget.attrs['class'] = 'form-control datepicker rounded'
        #visible.field.widget.attrs['type'] = 'date' this is overwritten by jquery ui datepicker
    elif 'send_to_' in visible.name:
        visible.field.widget.attrs['class'] = 'form-control rounded d-inline'
    else:
        visible.field.widget.attrs['class'] = 'form-control rounded'


class EntrepreneurForm(ModelForm):
    class Meta:
        model = Entrepreneur
        fields = ('identification_number', 'first_name', 'last_name', 'email', 'date_of_birth', 
                  'sex', 'phone_number', 'city',)
        labels = {
            'identification_number': 'cédula de identidad',
            'email': 'correo electrónico',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'date_of_birth': 'fecha de nacimiento',
            'sex': 'sexo',
            'phone_number': 'número de teléfono',
            'city': 'ciudad',
        }

    city = AutoCompleteSelectField('city', label="Ciudad", help_text='Ingresa el nombre de la ciudad o de su departamento', required=False)

    def __init__(self, *args, **kwargs):
        super(EntrepreneurForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'social_reason', 'rut', 'description', 'business_area', 'status', 'general_stage', 'entrepreneurs', 'postulation')
        labels = {            
            'name': 'nombre',
            'social_reason': 'razón social',
            'rut': 'RUT',
            'description': 'descripción',
            'business_area': 'sector de negocios',
            'status': 'estado',
            'general_stage': 'etapa general',
            'entrepreneurs': 'emprendedores',
            'postulation': 'postulación',
        }

    entrepreneurs = AutoCompleteSelectMultipleField('entrepreneurs', label='emprendedores', help_text='Búsqueda por CI o nombre')
    postulation = AutoCompleteSelectField('postulation',label='postulación' , help_text='Búqueda por CI del postulante, nombre del postulante o nombre del proyecto')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class ActivitiesForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'description', 'date', 'start_time', 'end_time', 'activity_type',
                  'inscription_deadline', 'attendance_limit', 'inscription_link')
        labels = {
            'title': 'nombre',
            'date': 'fecha',
            'start_time': 'hora de comienzo',
            'end_time': 'hora de finalización',
            'description': 'descripción',
            'activity_type': 'tipo de actividad',
            'inscription_deadline': 'cierre de inscripciones', 
            'attendance_limit': 'cupos',
            'inscription_link': 'código de inscripción (autogenerado)'
        }
    
    def __init__(self, *args, **kwargs):
        super(ActivitiesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if (visible.name == 'inscription_link'):
                visible.field.widget.attrs['readonly'] = True
            else:
                set_attribute(visible)

class BusinessAreaForm(ModelForm):
    class Meta:
        model = BusinessArea
        fields = ('name',)
        labels = {
          'name': 'nombre del sector',
        }
    
    def __init__(self, *args, **kwargs):
        super(BusinessAreaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():            
            set_attribute(visible)

class BroadcastAreaForm(ModelForm):
    class Meta:
        model = Broadcast
        fields = ('addressee', 'send_to_entrepreneurs', 'send_to_massive', 'activity', 'send_to_activity_inscriptions', 'subject', 'message', 'files')
        labels = {
            'addressee': 'recipientes',
            'activity': 'actividad',
            'send_to_activity_inscriptions': 'inscritos',
            'send_to_entrepreneurs': 'emprendedores',
            'send_to_massive': 'masivo',
            'subject': 'asunto',
            'message': 'mensaje',
            'files': 'archivos',
        }

    files = AutoCompleteSelectMultipleField('file', label='Archivos', help_text='Búsqueda por ID o nombre', required=False)
    activity = AutoCompleteSelectField('activity', label='Actividad', help_text='Búqueda por nombre, código de inscripción o ID de la actividad', required=False)

    def __init__(self, *args, **kwargs):
        super(BroadcastAreaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class FilesForm(ModelForm):
    class Meta:
        model = File
        fields = ('name', 'file_link', 'project', 'interview', 'entrepreneur', 'stage',)
        labels = {
            'name': 'nombre',
            'file_link': 'link',
            'project': 'proyecto',
            'interview': 'entrevista',
            'stage': 'etapa',
            'entrepreneur': 'emprendedor',
        }
    project = AutoCompleteSelectField('project', label='proyecto', help_text='Búqueda por nombre del proyecto, RUT o ID', required=False)
    interview = AutoCompleteSelectField('interview', label='entrevista', help_text='Búqueda por ID, nombre del proyecto, RUT o ID de la etapa', required=False)
    stage = AutoCompleteSelectField('stage', label='etapa', help_text='Búsqueda por RUT, nombre o ID del proyecto', required=False)
    entrepreneur = AutoCompleteSelectField('entrepreneurs', label='emprendedor', help_text='Búsqueda por CI o nombre', required=False)
    
    def __init__(self, *args, **kwargs):
        super(FilesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = ('date', 'interview_type', 'start_time', 'end_time', 'modality', 'stage', 'comments', 
                  'technicians',)
        labels = {
            'date': 'fecha',
            'interview_type': 'tipo de entrevista',
            'start_time': 'hora de inicio',
            'end_time': 'hora de fin',
            'modality': 'modalidad',
            'stage': 'etapa',
            'comments': 'comentarios',
            'technicians': 'técnicos',
        }

    stage = AutoCompleteSelectField('stage', label='Etapa', help_text='Búsqueda por RUT, nombre o ID del proyecto')
    technicians = AutoCompleteSelectMultipleField('technicians', label='técnicos', help_text='Búsqueda por CI o nombre')

    def __init__(self, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class PostulationForm(ModelForm):
    class Meta:
        model = Postulation
        fields = ('postulant', 'name', 'province', 'city', 'description', 'business_area', 'status', 'progress')
        labels = {
            'name': 'nombre del proyecto',
            'province': 'departamento',
            'city': 'ciudad',
            'postulant': 'postulante',
            'business_area': 'rubro',
            'description': 'descripción',
            'status': 'estado',
            'progress': 'progreso',
        }

    postulant = AutoCompleteSelectField('entrepreneurs', label='emprendedores', help_text='Búsqueda por CI o nombre')
    city = AutoCompleteSelectField('city', label="Ciudad", help_text='Ingresa el nombre de la ciudad o de su departamento', required=False)

    def __init__(self, *args, **kwargs):
        super(PostulationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class PostulationPublicForm(ModelForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellidos")
    email = forms.CharField(label="Correo electrónico")
    birth_date = forms.DateField(label='fecha de nacimiento')
    identification_number =  forms.IntegerField(label="Cédula (Sin puntos ni guiones)", min_value=1)
    sex = forms.ChoiceField(label="sexo", choices=Entrepreneur.SEX_CHOICES)
    phone = forms.CharField(label="teléfono/celular", required=True)

    class Meta:
        model = Postulation
        fields = ('first_name', 'last_name', 'identification_number', 'phone','email', 
        'birth_date', 'sex', 'province', 'city', 'name', 'description', 'business_area', 'progress')
        labels = {
            'name': 'nombre del proyecto',
            'business_area': 'rubro',
            'description': 'descripción',
            'province': 'departamento',
            'progress': 'progreso del proyecto',
        }

    city = AutoCompleteSelectField('city', label="Ciudad", help_text='Ingresa el nombre de la ciudad o de su departamento', required=False)

    def clean_email(self):
        mail = self.cleaned_data['email']
        if User.objects.filter(email=mail).exists():
            raise ValidationError("Ya existe una cuenta con este correo")
        return mail

    def clean_identification_number(self):
        ci = self.cleaned_data['identification_number']
        if User.objects.filter(identification_number=ci).exists():
            raise ValidationError("Ya existe una cuenta con la misma cédula")
        return ci

    def __init__(self, *args, **kwargs):
        super(PostulationPublicForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = ('stage_type', 'project', 'description', 'start_date', 'end_date')
        labels = {
            'stage_type': 'tipo',
            'project': 'proyecto',
            'description': 'descripción',
            'start_date': 'fecha de inicio',
            'end_date': 'fecha de finalización',
        }

    project = AutoCompleteSelectField('project', label='proyecto', help_text='Búqueda por nombre del proyecto, RUT o ID')
    def __init__(self, *args, **kwargs):
        super(StageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class TechnicianForm(ModelForm):
    class Meta:
        model = Technician
        fields = ('identification_number', 'first_name', 'last_name', 'email', 'phone_number',
                  'technician_speciality', 'technician_type', 'company')
        labels = {
            'identification_number': 'cédula de identidad',
            'email': 'correo',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'phone_number': 'número de teléfono',
            'technician_speciality': 'especialidad',
            'technician_type': 'tipo',
            'company': 'empresa',
        }
    
    def __init__(self, *args, **kwargs):
        super(TechnicianForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():          
            set_attribute(visible)

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ('name', 'province',)
        labels = {
            'name': 'nombre',
            'province': 'departamento',
        }

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class ProvinceForm(ModelForm):
    class Meta:
        model = Province
        fields = ('name',)
        labels = {
            'name': 'nombre',
        }

    def __init__(self, *args, **kwargs):
        super(ProvinceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class FinancingForm(ModelForm):
    class Meta:
        model = Financing
        fields = ('code', 'code_type', 'started_on_date', 'finished_on_date')
        labels = {
            'code': 'código de financiamiento',
            'code_type': 'tipo de financiamiento',
            'started_on_date': 'comenzado el:',
            'finished_on_date': 'finalizado el:',
        }

    def __init__(self, *args, **kwargs):
        super(FinancingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class InscriptionForm(ModelForm):
    class Meta:
        model = Inscription
        fields = ('email', 'first_name', 'assisted', 'last_name', 'phone_number', 'sex', 'province', 'city')
        labels = {
            'email': 'correo electrónico',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'phone_number': 'número de teléfono',
            'sex': 'sexo',
            'province': 'departamento',
            'assisted': 'asistencia',
        }

    city = AutoCompleteSelectField('city', label="Ciudad", help_text='Ingresa el nombre de la ciudad o de su departamento', required=False)
    def __init__(self, *args, **kwargs):
        super(InscriptionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class InscriptionPublicForm(ModelForm):
    class Meta:
        model = Inscription
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'sex', 'province', 'city')
        labels = {
            'email': 'correo electrónico',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'phone_number': 'número de teléfono',
            'sex': 'sexo',
            'province': 'departamento',
        }

    city = AutoCompleteSelectField('city', label="Ciudad", help_text='Ingresa el nombre de la ciudad o de su departamento', required=False)
    def __init__(self, *args, **kwargs):
        super(InscriptionPublicForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class FinancingForm(ModelForm):
    class Meta:
        model = Financing
        fields = ('project', 'code', 'code_type', 'started_on_date', 'finished_on_date')
        labels = {
            'project': 'proyecto',
            'code': 'código',
            'code_type': 'tipo',
            'started_on_date': 'fecha de inicio',
            'finished_on_date': 'fecha de finalización',
        }

    project = AutoCompleteSelectField('project', label='proyecto', help_text='Búqueda por nombre del proyecto, RUT o ID')

    def __init__(self, *args, **kwargs):
        super(FinancingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class TechnicianSpecialityForm(ModelForm):
    class Meta:
        model = TechnicianSpeciality
        fields = ('name',)
        labels = {
            'name': 'nombre',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('identification_number', 'first_name', 'last_name', 'username', 'phone_number', 'email',)
        labels = {
            'identification_number': 'cédula de identidad',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'username': 'nombre de usuario',
            'phone_number': 'teléfono',
            'email': 'correo',
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)


class SiteSettingsForm(ModelForm):
    class Meta:
        model = SiteSettings
        fields = ('postulation_page_title', 'postulation_page_description', 'postulation_page_info',)
        labels = {
            'postulation_page_title': 'Página de postulación: Título',
            'postulation_page_description': 'Página de postulación: Descripción',
            'postulation_page_info': 'Página de postulación: Información',
        }

    def __init__(self, *args, **kwargs):
        super(SiteSettingsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)