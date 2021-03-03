"""
Model Fields forms

This forms define the fields that are shown on the list page
"""

# Django
from django.forms import ModelForm, Form
from django import forms

# Models
from ..models import *
from ...accounts.models import User


class ActivitiesFieldsForm(ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'activity_type', 'date')
        labels = {
            'title': 'título',
            'activity_type': 'tipo',
            'date': 'fecha'
        }

class BusinessAreaFieldsForm(ModelForm):
    class Meta:
        model = BusinessArea
        fields = ('name',)
        labels = {
            'name': 'nombre',
        }

class BroadcastAreaFieldsForm(ModelForm):
    class Meta:
        model = Broadcast
        fields = ('subject',)
        labels = {
            'subject': 'Asunto',
        }

class EntrepreneurFieldsForm(ModelForm):
    class Meta:
        model = Entrepreneur
        fields = ('identification_number', 'email', 'first_name', 'last_name')
        labels = {
            'email': 'email',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'identification_number': 'C.I',
        }

class FilesFieldsForm(ModelForm):
    class Meta:
        model = File
        fields = ('name',)
        labels = {
            'name': 'nombre',
        }

class InterviewFieldsForm(ModelForm):
    stage_id = forms.IntegerField(label='Etapa')
    class Meta:
        model = Interview
        fields = ('stage_id', 'interview_type', 'date')
        labels = {
            'interview_type': 'tipo',
            'modality': 'modalidad',
            'date': 'fecha',
        }

class PostulationFieldsForm(Form):
    name = forms.CharField(label="nombre")
    status = forms.CharField(label="estado")
    created_at = forms.DateTimeField(label="Fecha")
    class Meta:
        model = Postulation
        labels = {
            'created_at': 'fecha',
        }

class ProjectFieldsForm(ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'status', 'rut')
        labels = {
            'name': 'Nombre',            
            'status': 'Estado',
            'rut': 'RUT',
        }

class StageFieldsForm(ModelForm):
    project_id = forms.IntegerField(label='Proyecto')
    class Meta:
        model = Stage
        fields = ('project_id', 'stage_type', 'start_date',)
        labels = {
            'stage_type': 'etapa',
            'start_date': 'inicio de etapa',
        }

class TechnicianFieldsForm(ModelForm):
    class Meta:
        model = Technician
        fields = ('identification_number', 'first_name', 'last_name', 'email')
        labels = {
            'identification_number': 'C.I',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'email': 'correo electrónico',         
        }

class CityFieldsForm(ModelForm):
    province_id = forms.IntegerField(label='Departamento')
    class Meta:
        model = City
        fields = ('name', 'province_id',)
        labels = {
            'name': 'Nombre',    
        }

class ProvinceFieldsForm(ModelForm):
    class Meta:
        model = Province
        fields = ('name',)
        labels = {
            'name': 'Nombre',    
        }

class FinancingsFieldsForm(ModelForm):
    project_id = forms.IntegerField(label='Proyecto')

    class Meta:
        model = Financing
        fields = ('project_id', 'code', 'code_type')
        labels = {
            'code': 'código',
            'code_type': 'tipo',    
        }

class InscriptionFieldsForm(ModelForm):
    class Meta:
        model = Inscription
        fields = ('email', 'first_name', 'last_name', 'assisted')
        labels = {
            'email': 'correo electrónico',
            'first_name': 'nombre',
            'last_name': 'apellido',
            'assisted': 'asistencia',
        }

class TechnicianSpecialityFieldsForm(ModelForm):
    class Meta:
        model = TechnicianSpeciality
        fields = ('name',)
        labels = {
            'name': 'nombre',
        }

class UserFieldsForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)
        labels = {
            'email': 'correo',
        }