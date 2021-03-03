"""
OBSOLOTE

Project views for front end"""

# Django
from django.views.generic import TemplateView
# Shortcuts
from django.shortcuts import render
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseServerError,
    HttpResponseRedirect,
)

# Rest framework
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Models
# Some IDEs might show this as an unresolved import
from bis.apps.incubator.models.projects import Project

# Forms
from bis.apps.incubator.forms.projects import ProjectForm


class Projects(TemplateView):
    template_name = 'gepiandashboard/projects/projects.html'
    context = {}

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        self.context['projects'] = Project.objects.filter() # TODO
        return render(request, self.template_name, self.context)


class ProjectsAddEditRemove(TemplateView): # TODO
    template_name = 'gepiandashboard/projects/addeditremoveproject.html'
    context = {}

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        project_id = self.kwargs.get('id', None)
        if project_id: # Edit or remove existing enterpreneur
            form = ProjectForm(request.POST, instance=get_object_or_404(Project, id=project_id))
        else: # Create new entrepreneur
            form = ProjectForm(request.POST)
            
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse('gepian:projects'))
        else:
            return HttpResponse('Formulario no válido:\n{0}'.format(form.errors)) # TODO

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        project_id = self.kwargs.get('id', None)
        if project_id:
            self.context['form'] = ProjectForm(instance=get_object_or_404(Project, id=project_id))
            self.context['project'] = Project.objects.get(id=project_id)
        else:
            self.context['form'] = ProjectForm()
            self.context['project'] = None
        return render(request, self.template_name, self.context)