"""Postulation page view"""

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

# Helper Dictionaries
from ...incubator.helpers.helperDictionaries import (
    getModel,
    getModelName,
    getModelForm,
)

# Form
from ...incubator.forms.modelForms import PostulationPublicForm

# Model
from ...incubator.models import City
from ...incubator.models import SiteSettings


class PostulationPage(TemplateView):
    template_name = 'gepiandashboard/pages/postulation.html'
    context = {}

    def createPostulant(self, first_name, last_name, email, birth_date, identification_number, sex, phone, city):
        birth_date_split = birth_date.split('/')
        city_instance = None
        if city and City.objects.filter(id=city).exists():
            city_instance = city_instance[0]
        postulant = getModel('entrepreneurs').objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            identification_number = identification_number,
            date_of_birth = '{0}-{1}-{2}'.format(birth_date_split[2], birth_date_split[1], birth_date_split[0]),
            sex = sex,
            phone_number=phone,
            city = city_instance,
        )
        return postulant

    def get(self, request, **kwargs):
        model_handle = 'postulations'
        model_form = PostulationPublicForm
        if not (model_form):
            return render(request, 'errors/404.html')
        self.context['form'] = model_form
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelName(model_handle)
        self.context['site_settings'] = SiteSettings.load()
        post_successful_postulate = request.session.get('post_successful_postulate_postulate', False)
        if (post_successful_postulate): 
            del(request.session['post_successful_postulate'])
            self.context['post_successful_postulate'] = True
        else:
            self.context['post_successful_postulate'] = False
        return render(request, self.template_name, self.context) #TODO add return link

    def post(self,request, *args, **kwargs):
        model_handle = 'postulations'
        queryDict = request.POST.copy()
        queryDict['status'] = '-'
        model_form = PostulationPublicForm(queryDict)
        if model_form.is_valid():
            try:
                newPostulant = self.createPostulant(
                    request.POST['first_name'],
                    request.POST['last_name'],
                    request.POST['email'],
                    request.POST['birth_date'],
                    request.POST['identification_number'],
                    request.POST['sex'],
                    request.POST['phone'],
                    request.POST['city'] or None)
            except:
                self.context['form'] = model_form
                self.context['model_handle'] = model_handle
                self.context['model_name'] = getModelName(model_handle)
                return render(request, self.template_name, self.context) # TODO
            post = model_form.save(commit=False)
            post.postulant = newPostulant
            post.save()
            request.session['post_successful_postulate'] = True
            return HttpResponseRedirect(reverse('gepian:postulate')) #TODO mensaje de que se envió con exito
        else:
            self.context['form'] = model_form
            self.context['model_handle'] = model_handle
            self.context['model_name'] = getModelName(model_handle)
            return render(request, self.template_name, self.context)
