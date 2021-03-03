"""
Model lookups for form fields

Github:
https://github.com/crucialfelix/django-ajax-selects
"""

# Ajax
from ajax_select import register, LookupChannel

# Models
from .models import (
    Activity,
    Entrepreneur, 
    BusinessArea,
    Postulation, 
    Technician,
    TechnicianSpeciality,
    Project, 
    Stage, 
    City, 
    Interview, 
    Broadcast, 
    File,
    Inscription,
    Financing,
    Province,
)

# Django
from django.urls import reverse


@register('entrepreneurs')
class EntrepreneursLookup(LookupChannel):

    model = Entrepreneur

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(identification_number__icontains=q)[:50]
        query_2 = self.model.objects.filter(first_name__icontains=q)[:50]
        query_3 = self.model.objects.filter(last_name__icontains=q)[:50]
        query_4 = self.model.objects.filter(email__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4
        search_result = matches.order_by('first_name')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'entrepreneurs', 'id': item.id})
        return '<a class="text-primary entrepreneur" href="{0}" target="__blank">↗ {1} · {2} {3}</a>'.format(
            url,
            item.identification_number, 
            item.first_name,
            item.last_name,)


@register('postulation')
class PostulationLookup(LookupChannel):

    model = Postulation

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(postulant__identification_number__icontains=q)[:50]
        query_3 = self.model.objects.filter(postulant__first_name__icontains=q)[:50]
        query_4 = self.model.objects.filter(postulant__last_name__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'postulations', 'id': item.id})
        return '<a class="text-primary postulation" href="{0}" target="__blank">↗ {1} · {2} · {3} {4}</a>'.format(
            url,
            item.name,
            item.postulant.identification_number, 
            item.postulant.first_name, 
            item.postulant.last_name
        )

@register('technicians')
class TechniciansLookup(LookupChannel):

    model = Technician

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(identification_number__icontains=q)[:50]
        query_2 = self.model.objects.filter(first_name__icontains=q)[:50]
        query_3 = self.model.objects.filter(last_name__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('first_name')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'technicians', 'id': item.id})
        return '<a class="text-primary technician" href="{0}" target="__blank">↗ {1} · {2} {3}</a>'.format(
            url,
            item.identification_number, 
            item.first_name,
            item.last_name)


@register('project')
class ProjectLookup(LookupChannel):

    model = Project

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(rut__icontains=q)[:50]
        query_3 = self.model.objects.filter(id__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('name')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'projects', 'id': item.id})
        return '<a class="text-primary project" href="{0}" target="__blank">↗ {1} · {2}</a>'.format(url, item.rut, item.name)


@register('stage')
class StageLookup(LookupChannel):

    model = Stage

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(project__rut__icontains=q)[:50]
        query_2 = self.model.objects.filter(project__name__icontains=q)[:50]
        query_3 = self.model.objects.filter(project__id__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'stages', 'id': item.id})
        return '<a class="text-primary stage" href="{0}" target="__blank">↗ #{1} · {2} · {3}</a>'.format(url, item.id, item.project.name, item.get_stage_type_display())


@register('city')
class CityLookup(LookupChannel):

    model = City

    def check_auth(user, model):
        return True

    def can_add(self, user, model):
        return True

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(province__name__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('name')[:50]
        return search_result

    def format_item_display(self, item):
        return '<span class="city">{0}</span>'.format(item.name)

    def format_match(self, item):
        province = item.province.name
        if not province:
            return '<span class="city">{0}</span>'.format(item.name)
        return '<span class="city">{0} - {1}</span>'.format(item.name, province)


@register('interview')
class InterviewLookup(LookupChannel):

    model = Interview

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(stage__project__rut__icontains=q)[:50]
        query_3 = self.model.objects.filter(stage__project__name__icontains=q)[:50]
        query_4 = self.model.objects.filter(stage__project__id__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'interviews', 'id': item.id})
        return '<a class="text-primary interview" href="{0}" target="__blank">↗ #{1} · {2} ({3})</a>'.format(url, item.id, item.stage.project.name, item.get_interview_type_display())

@register('broadcast')
class BroadcastLookup(LookupChannel):

    model = Broadcast

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(subject__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return '<span class="broadcast">#{0} · {1}</span>'.format(item.id, item.subject)


@register('file')
class FileLookup(LookupChannel):

    model = File

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(name__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'files', 'id': item.id})
        return '<a class="text-primary file" href="{0}" target="__blank">↗#{1} · {2}</a>'.format(url, item.id, item.name)


@register('activity')
class ActivityLookup(LookupChannel):

    model = Activity

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(title__icontains=q)[:50]
        query_2 = self.model.objects.filter(id__icontains=q)[:50]
        query_3 = self.model.objects.filter(inscription_link__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'activities', 'id': item.id})
        return '<a class="text-primary activity" href="{0}" target="__blank">↗ {1}<a/>'.format(url, item.title)


# General search lookups start

@register('inscriptiongeneral')
class InscriptionGeneralLookup(LookupChannel):

    model = Inscription

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(email__icontains=q)[:50]
        query_3 = self.model.objects.filter(first_name__icontains=q)[:50]
        query_4 = self.model.objects.filter(last_name__icontains=q)[:50]
        query_5 = self.model.objects.filter(activity_inscriptions__title__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4 | query_5
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericeditmodel", kwargs={'model': 'inscriptions', 'id': item.id})
        assisted =  '✘'
        if item.assisted:
            assisted = '✓'
        try:
            return '<a class="text-primary inscription" href="{0}" target="__blank">↗ {1} {2} · {3} ({4})<a/>'.format(url, item.first_name, item.last_name, item.activity_inscriptions.get().title, assisted)
        except Exception as e:
            print('Exception:', e)
            return '<a class="text-primary inscription" href="{0}" target="__blank">↗ #{1} {2} · {2} ({3})<a/>'.format(url, item.id, item.first_name, item.last_name, assisted)


@register('entrepreneurgeneral')
class EntrepreneurGeneralLookup(LookupChannel):

    model = Entrepreneur

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(identification_number__icontains=q)[:50]
        query_2 = self.model.objects.filter(first_name__icontains=q)[:50]
        query_3 = self.model.objects.filter(last_name__icontains=q)[:50]
        query_4 = self.model.objects.filter(email__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4
        search_result = matches.order_by('first_name')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'entrepreneurs', 'id': item.id})
        return '<a class="text-primary entrepreneur" href="{0}" target="__blank">↗ {1} {2} · {3}<a/>'.format(url, item.first_name, item.last_name, item.identification_number)


@register('projectgeneral')
class ProjectGeneralLookup(LookupChannel):

    model = Project

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(rut__icontains=q)[:50]
        query_3 = self.model.objects.filter(id__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('name')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'projects', 'id': item.id})
        return '<a class="text-primary project" href="{0}" target="__blank">↗ {1} · {2}<a/>'.format(url, item.name, item.rut)

@register('interviewgeneral')
class InterviewGeneralLookup(LookupChannel):

    model = Interview

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(stage__project__rut__icontains=q)[:50]
        query_3 = self.model.objects.filter(stage__project__name__icontains=q)[:50]
        query_4 = self.model.objects.filter(stage__project__id__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'interviews', 'id': item.id})
        return '<a class="text-primary interview" href="{0}" target="__blank">↗ {1} · {2}<a/>'.format(url, item.stage.project.name, item.get_interview_type_display())


@register('stagegeneral')
class StageGeneralLookup(LookupChannel):

    model = Stage

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(project__rut__icontains=q)[:50]
        query_2 = self.model.objects.filter(project__name__icontains=q)[:50]
        query_3 = self.model.objects.filter(project__id__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'stages', 'id': item.id})
        return '<a class="text-primary stage" href="{0}" target="__blank">↗ {1} · {2}<a/>'.format(url, item.project.name, item.get_stage_type_display())


@register('postulationgeneral')
class PostulationGeneralLookup(LookupChannel):

    model = Postulation

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(postulant__identification_number__icontains=q)[:50]
        query_3 = self.model.objects.filter(postulant__first_name__icontains=q)[:50]
        query_4 = self.model.objects.filter(postulant__last_name__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'postulations', 'id': item.id})
        return '<a class="text-primary postulation" href="{0}" target="__blank">↗ {1} · {2} · {3} {4}<a/>'.format(
            url, 
            item.name,
            item.postulant.first_name, 
            item.postulant.last_name,
            item.postulant.identification_number)


@register('activitygeneral')
class ActivityGeneralLookup(LookupChannel):

    model = Activity

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(title__icontains=q)[:50]
        query_2 = self.model.objects.filter(id__icontains=q)[:50]
        query_3 = self.model.objects.filter(inscription_link__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'activities', 'id': item.id})
        return '<a class="text-primary activity" href="{0}" target="__blank">↗ {1}<a/>'.format(url, item.title)


@register('financinggeneral')
class FinancingGeneralLookup(LookupChannel):

    model = Financing

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(code__icontains=q)[:50]
        query_2 = self.model.objects.filter(project__name__icontains=q)[:50]
        query_3 = self.model.objects.filter(project__rut__icontains=q)[:50]
        query_4 = self.model.objects.filter(project__id__icontains=q)[:50]
        matches = query_1 | query_2 | query_3 | query_4
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'financings', 'id': item.id})
        return '<a class="text-primary financing" href="{0}" target="__blank">↗ {1} · {2}<a/>'.format(url, item.project.name, item.code)


@register('broadcastgeneral')
class BroadcastGeneralLookup(LookupChannel):

    model = Broadcast

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(subject__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'broadcasts', 'id': item.id})
        subject = 'Sin asunto'
        if item.subject:
            subject = item.subject
        return '<a class="text-primary broadcast" href="{0}" target="__blank">↗ #{1} · {2}<a/>'.format(url, item.id, subject)


@register('provincegeneral')
class ProvinceGeneralLookup(LookupChannel):

    model = Province

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(name__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('name')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'provinces', 'id': item.id})
        return '<a class="text-primary province" href="{0}" target="__blank">↗ #{1} · {2}<a/>'.format(url, item.id, item.name)

@register('citygeneral')
class CityGeneralLookup(LookupChannel):

    model = City

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(province__name__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('name')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'cities', 'id': item.id})
        return '<a class="text-primary city" href="{0}" target="__blank">↗ {1} · {2}<a/>'.format(url, item.name, item.province)


@register('techniciangeneral')
class TechnicianGeneralLookup(LookupChannel):

    model = Technician

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(identification_number__icontains=q)[:50]
        query_2 = self.model.objects.filter(first_name__icontains=q)[:50]
        query_3 = self.model.objects.filter(last_name__icontains=q)[:50]
        matches = query_1 | query_2 | query_3
        search_result = matches.order_by('first_name')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'technicians', 'id': item.id})
        return '<a class="text-primary technician" href="{0}" target="__blank">↗ {1} {2}<a/>'.format(url, item.first_name, item.last_name)


@register('technicianspecialitygeneral')
class TechnicianSpecialityGeneralLookup(LookupChannel):

    model = TechnicianSpeciality

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(id__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'technicianspecialities', 'id': item.id})
        return '<a class="text-primary technicianspeciality" href="{0}" target="__blank">↗ {1}<a/>'.format(url, item.name)

@register('businessareageneral')
class BusinessAreaGeneralLookup(LookupChannel):

    model = BusinessArea

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(name__icontains=q)[:50]
        query_2 = self.model.objects.filter(id__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'businessareas', 'id': item.id})
        return '<a class="text-primary businessarea" href="{0}" target="__blank">↗ {1}<a/>'.format(url, item.name)

@register('filegeneral')
class FileGeneralLookup(LookupChannel):

    model = File

    def get_query(self, q, request):
        query_1 = self.model.objects.filter(id__icontains=q)[:50]
        query_2 = self.model.objects.filter(name__icontains=q)[:50]
        matches = query_1 | query_2
        search_result = matches.order_by('created_at')[:50]
        return search_result

    def format_item_display(self, item):
        return ''

    def format_match(self, item):
        url = reverse("gepian:genericviewmodel", kwargs={'model': 'files', 'id': item.id})
        return '<a class="text-primary file" href="{0}" target="__blank">↗ #{1} · {2}<a/>'.format(url, item.id, item.name)