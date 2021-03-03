"""User views"""

# Django
from bis.apps.incubator.models.entrepreneurs import Entrepreneur
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
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

# Models
from ..models import User

# Exception
from django.core.exceptions import ObjectDoesNotExist


class UserLogin(TemplateView):
    authentication_classes = []
    permission_classes = []
    template_name = 'accounts/login.html'
    context = {}

    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = authenticate(username=email, password=password)
        if user:
            is_entrepreneur = False
            try:
                # Prevent entrepreneurs from accessing
                is_entrepreneur = Entrepreneur.objects.get(id=user.id)
            except ObjectDoesNotExist:
                pass
            if user.is_active and (not is_entrepreneur):
                login(self.request, user)
                return HttpResponseRedirect(reverse('gepian:dashboardindex'))
            else:
                self.context['errors'] = ['El usuario no está activo']
                return render(request, self.template_name, self.context)
        else:
            """if (User.objects.filter(email=email).exists()):
                self.context['errors'] = ['Contraseña incorrecta']
            else:
                self.context['errors'] = ['Dirección de correo incorrecta']"""
            self.context['errors'] = ['Dirección de correo o contraseña incorrectos']
            return render(request, self.template_name, self.context)
    
    def get(self, request):
        #if request.user.is_authenticated:
            # return HttpResponseRedirect(reverse('gepian:dashboardindex'))
        self.context['errors'] = None
        return render(request, self.template_name, self.context)
        

class UserLogout(TemplateView): # TODO Is this really a Templateview??
    authentication_classes = []
    permission_classes = []
    template_name = 'accounts/login.html'
    context = {}
    
    def get(self, request):
        if request.user.is_authenticated:
            logout(self.request)
        return HttpResponseRedirect(reverse('users:login'))
