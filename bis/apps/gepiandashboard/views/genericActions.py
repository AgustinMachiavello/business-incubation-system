"""Add edit remove generic template view"""

# Django
from django.db.models import query
from bis.apps.accounts import models
from bis.apps.incubator.models.entrepreneurs import Entrepreneur
from bis.apps.accounts.models.users import User
from bis.apps.incubator.models.activities import Activity
from django.views.generic import TemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.sites.models import Site
from django.db.models.deletion import ProtectedError

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
    FORM_FIELDS_DICT,
    FORM_DICT,
    MODEL_DICT,
    MODEL_NAME_DICT,
    MODEL_FILTER_DICT,
    getModel,
    getModelName,
    getModelPluralName,
    getModelForm,
    getModelFieldsForm,
    getModelFilters,
    getAvailableFilters,
    getModelAnalytics,
    getModelQuickViewSerializer,
    getModelGeneralSearchForm,
)

# Datetime
from datetime import datetime, date

# Emails
from ...incubator.views.emails import startSendEmails, generateInscriptionAlertMessage

# Forms
from ...incubator.forms.modelForms import InscriptionPublicForm


class GenericAddModel(TemplateView):
    template_name = 'gepiandashboard/generic/addmodel.html'
    template_name_redirect = 'gepiandashboard/generic/listmodel.html'
    context = {}

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not (model_handle):
            return render(request, 'errors/404.html')
        model_form = getModelForm(model_handle)
        if not (model_form):
            return render(request, 'errors/404.html')
        self.context['form'] = model_form
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelPluralName(model_handle)
        self.context['model_name_singular'] = getModelName(model_handle)
        return render(request, self.template_name, self.context)

    def post(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not (model_handle):
            return render(request, 'errors/404.html')
        model_form = getModelForm(model_handle)
        if not (model_form):
            return render(request, 'errors/404.html')
        model_form = model_form(request.POST)
        if model_form.is_valid():
            if model_handle == 'projects':
                post = model_form.save(commit=False)
                post.registered_by = request.user
                post = post.save()
            else:
                post = model_form.save()
            return HttpResponseRedirect(reverse('gepian:genericlistmodel', kwargs={'model': model_handle})) # TODO hacer que vuelva a la LIST PAGE
        else:
            self.context['form'] = model_form
            self.context['model_handle'] = model_handle
            self.context['model_name'] = getModelPluralName(model_handle)
            self.context['model_name_singular'] = getModelName(model_handle)
            return render(request, self.template_name, self.context) # TODO


class GenericListModel(TemplateView):
    template_name = 'gepiandashboard/generic/listmodel.html'
    context = {}
    items_per_page = 25
    
    def handle_url_filters(self, request, model):
        available_filters = getAvailableFilters()
        filters = {}
        if model == User:
            filters['is_staff'] = True
        order_by = None
        active_filters = {}
        for param, value in request.GET.items():
            if param == 'assisted':
                if param in available_filters:
                    filters[param] = True if value == 'true' else False
                    active_filters[param] = True if value == 'true' else False
            elif param != 'order_by':
                if param in available_filters:
                    filters[param] = value
                    active_filters[param] = value
            else:
                order_by = value
        queryset = model.objects.filter(**filters)
        if order_by:
            queryset = queryset.order_by(order_by)
        return [queryset.values(), active_filters]

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not model_handle:
            return render(request, 'errors/404.html')
        model_fields_form = getModelFieldsForm(model_handle)
        if not (model_fields_form):
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')

        dataset = self.handle_url_filters(request, model)
        instances = dataset[0]
        paginator = Paginator(instances, self.items_per_page) # Show 25 per page
        page = request.GET.get('page')
        try:
            instances = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            instances = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            instances = paginator.page(paginator.num_pages)

        for inst in instances:
            temp_inst = get_object_or_404(model, id=inst['id'])
            inst['instance'] = temp_inst
            inst['instance_serialized'] = getModelQuickViewSerializer(model_handle)(temp_inst).data

        self.context['model_objects_dict'] = instances # instances

        self.context['active_filters'] = dataset[1]
        self.context['fields_form'] = model_fields_form
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelPluralName(model_handle)
        self.context['model_name_singular'] = getModelName(model_handle)
        self.context['model_objects_filter_dict'] = getModelFilters(model_handle)

        self.context['extra_filter'] = None
        if model_handle == 'inscriptions':
            activity = request.GET.get('activity_inscriptions', None)
            try:
                activity = Activity.objects.get(id=activity)
                self.context['extra_filter'] = activity
            except Exception as e:
                print('Expeciton:', e)
                pass

        self.context['general_search_form'] = getModelGeneralSearchForm(model_handle)

        post_successful = request.session.get('post_successful', False)
        post_delete_successful = request.session.get('post_delete_successful', False)

        if (post_successful): 
            del(request.session['post_successful'])
            self.context['post_successful'] = True
        else:
            self.context['post_successful'] = False
        if (post_delete_successful): 
            del(request.session['post_delete_successful'])
            self.context['post_delete_successful'] = True
        else:
            self.context['post_delete_successful'] = False   
        return render(request, self.template_name, self.context)


class GenericEditModel(TemplateView):
    template_name = 'gepiandashboard/generic/editmodel.html'
    template_name_redirect = 'gepiandashboard/generic/listmodel.html'
    template_name_redirect_administration = 'gepiandashboard/pages/administration_index.html'
    context = {}

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not model_handle:
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')
        model_id = self.kwargs.get('id', None)
        if not (model_id):
            return render(request, 'errors/404.html')
        model_form = getModelForm(model_handle)
        if not (model_form):
            return render(request, 'errors/404.html')
        self.context['form'] = model_form(instance=get_object_or_404(model, id=model_id))
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelPluralName(model_handle)
        self.context['model_name_singular'] = getModelName(model_handle)
        self.context['model_instance'] = get_object_or_404(model, id=model_id)
        return render(request, self.template_name, self.context)

    def post(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not model_handle:
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')
        model_id = self.kwargs.get('id', None)
        if not (model_id):
            return render(request, 'errors/404.html')
        model_form = getModelForm(model_handle)
        if not (model_form):
            return render(request, 'errors/404.html')
        model_form = model_form(request.POST, instance=get_object_or_404(model, id=model_id))
        self.context['form'] = model_form
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelPluralName(model_handle)
        self.context['model_name_singular'] = getModelName(model_handle)
        if model_form.is_valid():
            post = model_form.save()
            request.session['post_successful'] = True
            if model_handle not in ['sitesettings']:
                return redirect(reverse('gepian:genericlistmodel', kwargs={'model': model_handle}), self.template_name_redirect, self.context)
            else:
                return redirect(reverse('gepian:administrationindex'), self.template_name_redirect_administration, self.context)
        else:
            return render(request, self.template_name, self.context)


class GenericDeleteModel(TemplateView):
    template_name = 'gepiandashboard/generic/deletemodel.html'
    template_name_redirect = 'gepiandashboard/generic/listmodel.html'
    context = {}

    def get(self, request, **kwargs):
        # delete confirmation page
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not model_handle:
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')
        model_id = self.kwargs.get('id', None)
        if not (model_id):
            return render(request, 'errors/404.html')
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelName(model_handle)
        self.context['model_instance'] = get_object_or_404(model, id=model_id)
        delete_error = request.session.get('delete_error', False)
        if (delete_error): 
            del(request.session['delete_error'])
            self.context['delete_error'] = delete_error
        else:
            self.context['delete_error'] = False
        return render(request, self.template_name, self.context)

    def post(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not model_handle:
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')
        model_id = self.kwargs.get('id', None)
        if not (model_id):
            return render(request, 'errors/404.html')
        instance = get_object_or_404(model, id=model_id)
        self.context['delete_error'] = False
        try:
            instance.delete() # delete
            request.session['post_delete_successful'] = True
        except ProtectedError as e:
            print('Expection:', e)
            self.context['delete_error'] = 'El emprendedor que intentas eliminar está ascoiado a una postulación. Elimina la postulación para proceder.'
            return render(request, self.template_name, self.context)
        except Exception as e:
            print('Expection:', e)
            self.context['delete_error'] = e
            return render(request, self.template_name, self.context)
        return redirect(reverse('gepian:genericlistmodel', kwargs={'model': model_handle}), self.template_name_redirect, self.context)


class GenericModelReportPage(TemplateView):
    template_name = 'gepiandashboard/generic/reportmodel.html'
    context = {}

    def handle_url_filters(self, request, model):
        available_filters = getAvailableFilters()
        privateFilters = ['order_by']
        filters = {}
        order_by = None
        active_filters = {}
        for param, value in request.GET.items():
            if param not in privateFilters:
                if param in available_filters:
                    filters[param] = value[0]
                    active_filters[param] = value[0]
            else:
                if param == 'order_by':
                    order_by = value
        queryset = model.objects.filter(**filters)
        if order_by:
            queryset = queryset.order_by(order_by)
        return [queryset.values(), active_filters]

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not model_handle:
            return render(request, 'errors/404.html')
        model_fields_form = getModelFieldsForm(model_handle)
        if not (model_fields_form):
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')
        self.context['fields_form'] = model_fields_form
        self.context['model_handle'] = model_handle
        self.context['model_export'] = model_handle + '__count'
        self.context['model_name'] = getModelPluralName(model_handle)
        self.context['model_name_singular'] = getModelName(model_handle)
        self.context['model_objects_filter_dict'] = getModelFilters(model_handle)
        dataset = self.handle_url_filters(request, model)
        self.context['model_objects_dict'] = dataset[0]
        self.context['active_filters'] = dataset[1]
        self.context['model_analytics_dict'] = getModelAnalytics(model_handle)
        dateFrom = None
        dateTo = None
        for param, value in request.GET.items():
            if param == 'date_from':
                dateFrom = value.replace('-', '/')
            elif param == 'date_to':
                dateTo = value.replace('-', '/')
        self.context['dateFrom'] = dateFrom
        self.context['dateTo'] = dateTo
        return render(request, self.template_name, self.context)


class GenericActivityInscription(TemplateView):
    template_name = 'gepiandashboard/generic/inscription.html'
    template_name_redirect = 'gepiandashboard/generic/inscription.html'
    context = {}

    def get(self, request, **kwargs):
        model_handle = 'inscriptions'
        if not model_handle:
            return render(request, 'errors/404.html')
        model_form = InscriptionPublicForm
        if not model_form:
            return render(request, 'errors/404.html')
        inscription_code = self.kwargs.get('inscription_code', None)
        if not inscription_code:
            return render(request, 'errors/404.html')
        activity = get_object_or_404(getModel('activities'), inscription_link=inscription_code)
        self.context['form'] = model_form
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelName(model_handle)
        self.context['activity'] = activity 
        post_successful = request.session.get('post_successful', False)
        post_error = request.session.get('post_error', False)
        if (post_successful): 
            del(request.session['post_successful'])
            self.context['post_successful'] = True
        else:
            self.context['post_successful'] = False
        if (post_error): 
            del(request.session['post_error'])
            self.context['post_error'] = True
        else:
            self.context['post_error'] = False

        self.context['deadline_available'] = True
        if (activity.inscription_deadline and date.today() > activity.inscription_deadline):
            self.context['deadline_available'] = False
        return render(request, self.template_name, self.context)

    def post(self, request, **kwargs):
        model_handle = 'inscriptions'
        if not model_handle:
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')
        inscription_code = self.kwargs.get('inscription_code', None)
        if not inscription_code:
            return render(request, 'errors/404.html')
        model_form = getModelForm(model_handle)
        if not (model_form):
            return render(request, 'errors/404.html')
        model_form = model_form(request.POST)
        activity = get_object_or_404(getModel('activities'), inscription_link=inscription_code)
        self.context['form'] = model_form
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelName(model_handle)
        if model_form.is_valid():
            if (activity.attendance_limit and activity.inscriptions.count() >= activity.attendance_limit):
                    request.session['post_error'] = 'Límite de cupos alcanzado.'
                    return redirect(reverse('gepian:inscription', kwargs={'inscription_code': inscription_code}), self.template_name_redirect, self.context)
            try:
                already_present = activity.inscriptions.filter(email=request.POST['email']).exists()
                if not already_present:
                    post = model_form.save() # save inscription
                    activity.inscriptions.add(post) # add inscription to activity
                    request.session['post_successful'] = True
                    message = generateInscriptionAlertMessage(request.POST['first_name'], activity, post)
                    startSendEmails(addressee_list=[request.POST['email']], message=message, subject='Inscripción a evento' )
                else:
                    request.session['post_error'] = True
                    return redirect(reverse('gepian:inscription', kwargs={'inscription_code': inscription_code}), self.template_name_redirect, self.context)
            except Exception as e:
                print('Exception:', e)
                request.session['post_error'] = True
            return redirect(reverse('gepian:inscription', kwargs={'inscription_code': inscription_code}), self.template_name_redirect, self.context)
        else:
            return render(request, self.template_name, self.context)


class GenericQuickViewModel(TemplateView):
    template_name = 'gepiandashboard/generic/viewmodel.html'
    context = {}

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        model_handle = self.kwargs.get('model', None)
        if not model_handle:
            return render(request, 'errors/404.html')
        model = getModel(model_handle)
        if not (model):
            return render(request, 'errors/404.html')
        model_id = self.kwargs.get('id', None)
        if not (model_id):
            return render(request, 'errors/404.html')
        """model_form = getModelForm(model_handle)
        if not (model_form):
            return render(request, 'errors/404.html')
        self.context['form'] = model_form(instance=get_object_or_404(model, id=model_id))"""
        self.context['model_handle'] = model_handle
        self.context['model_name'] = getModelName(model_handle)
        self.context['model_instance'] = get_object_or_404(model, id=model_id)
        self.context['model_instance_serialized'] = getModelQuickViewSerializer(model_handle)(get_object_or_404(model, id=model_id)).data
        self.context['model_name_singular'] = getModelName(model_handle)
        return render(request, self.template_name, self.context)