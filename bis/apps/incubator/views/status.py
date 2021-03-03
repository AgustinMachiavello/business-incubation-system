"""
Data status sender (only admin users)
"""

# Django Rest framework
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)
from django.shortcuts import render

# Emails
from ..views.emails import startSendEmails, generateStatusReportMessage

# Threading
import threading

# DB
from ....settings import base

from django.http import (
    JsonResponse,
)

# Site
from django.contrib.sites.models import Site


class StatusReport(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None, *args, **kwargs):
        addresse = request.GET.get('email', None)
        email_list = []
        if addresse:
            email_list = [addresse]
        messages = {}
        current_site = Site.objects.get_current()
        messages['domain'] = current_site.domain
        messages['active_threads'] =  threading.active_count()
        messages['database_engine'] = base.DATABASES['default']['ENGINE']
        messages['database_name'] = base.DATABASES['default']['NAME']
        messages['email_host_user'] = base.EMAIL_HOST_USER
        messages['email_port'] = base.EMAIL_PORT
        messages['static_root'] = base.STATIC_ROOT
        messages['allowed_hosts'] = base.ALLOWED_HOSTS

        if len(email_list) > 0:
            message = generateStatusReportMessage(messages)
            startSendEmails(addressee_list=email_list, message=message, subject='Status report: {0}'.format(addresse))
            messages['addresse'] = addresse
        return JsonResponse(messages, content_type="application/json")
        