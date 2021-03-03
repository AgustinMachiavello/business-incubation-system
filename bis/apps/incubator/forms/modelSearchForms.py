"""
Model search forms
"""


# Django
from django.forms import ModelForm, Form
from django import forms

# Ajax autocomplete
from ajax_select.fields import AutoCompleteSelectField

from ..models.inscriptions import Inscription


def set_attribute(visible):
    if ('search_bar' in visible.name):
        visible.field.widget.attrs['class'] = 'form-control rounded'
        visible.field.widget.attrs['placeholder'] = 'Buscar...'
        visible.field.widget.attrs['id'] = 'searchbox'
    elif ('date' in visible.name or visible.name in ['inscription_deadline'] ):
        visible.field.widget.attrs['class'] = 'form-control datepicker rounded'
    else:
        visible.field.widget.attrs['class'] = 'form-control rounded'


class InscriptionGeneralSearchForm(Form):
    inscription_search_bar = AutoCompleteSelectField('inscriptiongeneral', label='',
        help_text='Búqueda correo o nombre de la persona inscrita', required=False)

    def __init__(self, *args, **kwargs):
        super(InscriptionGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class EntrepreneurGeneralSearchForm(Form):
    entrepreneur_search_bar = AutoCompleteSelectField('entrepreneurgeneral', label='',
        help_text='Búqueda por CI o nombre', required=False)

    def __init__(self, *args, **kwargs):
        super(EntrepreneurGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class ProjectGeneralSearchForm(Form):
    project_search_bar = AutoCompleteSelectField('projectgeneral', label='',
        help_text='Búqueda por nombre o RUT', required=False)

    def __init__(self, *args, **kwargs):
        super(ProjectGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class InterviewGeneralSearchForm(Form):
    interview_search_bar = AutoCompleteSelectField('interviewgeneral', label='',
        help_text='Búqueda por ID, nombre del proyecto, RUT o ID de la etapa', required=False)

    def __init__(self, *args, **kwargs):
        super(InterviewGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class StageGeneralSearchForm(Form):
    stage_search_bar = AutoCompleteSelectField('stagegeneral', label='',
        help_text='Búsqueda por RUT, nombre o ID del proyecto', required=False)

    def __init__(self, *args, **kwargs):
        super(StageGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class PostulationGeneralSearchForm(Form):
    postulation_search_bar = AutoCompleteSelectField('postulationgeneral', label='',
        help_text='Búqueda por CI del postulante, nombre del postulante o nombre del proyecto', required=False)

    def __init__(self, *args, **kwargs):
        super(PostulationGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class ActivityGeneralSearchForm(Form):
    activity_search_bar = AutoCompleteSelectField('activitygeneral', label='',
        help_text='Búqueda por nombre, código de inscripción o ID de la actividad', required=False)

    def __init__(self, *args, **kwargs):
        super(ActivityGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class FinancingGeneralSearchForm(Form):
    financing_search_bar = AutoCompleteSelectField('financinggeneral', label='',
        help_text='Búqueda por nombre codigo, o RUT, nombre, ID del proyecto', required=False)

    def __init__(self, *args, **kwargs):
        super(FinancingGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class BroadcastGeneralSearchForm(Form):
    broadcast_search_bar = AutoCompleteSelectField('broadcastgeneral', label='',
        help_text='Búqueda por id o asunto', required=False)

    def __init__(self, *args, **kwargs):
        super(BroadcastGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class ProvinceGeneralSearchForm(Form):
    province_search_bar = AutoCompleteSelectField('provincegeneral', label='',
        help_text='Búqueda por id o nombre', required=False)

    def __init__(self, *args, **kwargs):
        super(ProvinceGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)


class CityGeneralSearchForm(Form):
    city_search_bar = AutoCompleteSelectField('citygeneral', label='',
        help_text='Búsqueda por el nombre de la ciudad o de su departamento', required=False)

    def __init__(self, *args, **kwargs):
        super(CityGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class TechnicianGeneralSearchForm(Form):
    technician_search_bar = AutoCompleteSelectField('techniciangeneral', label='',
        help_text='Búsqueda por CI o nombre', required=False)

    def __init__(self, *args, **kwargs):
        super(TechnicianGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class TechnicianSpecialityGeneralSearchForm(Form):
    technician_search_bar = AutoCompleteSelectField('technicianspecialitygeneral', label='',
        help_text='Búsqueda por nombre', required=False)

    def __init__(self, *args, **kwargs):
        super(TechnicianSpecialityGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class BusinessAreaGeneralSearchForm(Form):
    businessarea_search_bar = AutoCompleteSelectField('businessareageneral', label='',
        help_text='Búsqueda por nombre', required=False)

    def __init__(self, *args, **kwargs):
        super(BusinessAreaGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)

class FileGeneralSearchForm(Form):
    file_search_bar = AutoCompleteSelectField('filegeneral', label='',
        help_text='Búsqueda por nombre o ID', required=False)

    def __init__(self, *args, **kwargs):
        super(FileGeneralSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            set_attribute(visible)