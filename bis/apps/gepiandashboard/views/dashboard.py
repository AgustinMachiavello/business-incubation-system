"""Dashboard views"""

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

# Analytics
from ...incubator.helpers.helperDictionaries import getHomeIndexAnalytics


class DashboardIndex(TemplateView):
    template_name = 'gepiandashboard/pages/dashboardindex.html'
    context = {}

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        self.context['analytics'] = getHomeIndexAnalytics()
        return render(request, self.template_name, self.context)
