"""Administration views"""

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

# Menus
from ...incubator.helpers.helperDictionaries import getAdministrationIndexMenus


class AdministrationIndex(TemplateView):
    template_name = 'gepiandashboard/pages/administration_index.html'
    context = {}

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        self.context['menus'] = getAdministrationIndexMenus()
        return render(request, self.template_name, self.context)
