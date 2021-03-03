""" Analytics views """

# Django
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseServerError,
    HttpResponseRedirect,
    JsonResponse,
)

# Django Rest framework
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
)

# Models
from ..models import *

# Helpers
from ..helpers import queryFilters, helperDictionaries

# Datetime
from datetime import datetime, timedelta

# custom analytics
from .customAnalytics import getModelCountHistory, getModelCount, getHistoryLabels, ANALYTICS_DICT


def handleAnalytic(analyticsHandle, date_from=None, date_to=None):
    output = {
        'data': [],
        'labels': [],
        'value': 0,
    }
    if ('__' in analyticsHandle):
        tempAnalyticHandle = analyticsHandle.split('__')
        modelHandle = tempAnalyticHandle[0]
        model = helperDictionaries.getModel(modelHandle)
        fieldsDict = helperDictionaries.getModelReportFields(modelHandle)
        fields = [*fieldsDict.keys()]
        fieldLabels = [*fieldsDict.values()]
        queryset = helperDictionaries.getModel(modelHandle).objects
        if date_from:
            queryset = queryset.filter(created_at__gte=date_from)
        if date_to:
            queryset = queryset.filter(created_at__lte=date_to)
        if ('__count' in analyticsHandle):
            output['data'] =  getModelCountHistory(queryset)
            output['labels'] = getHistoryLabels(queryset)
            output['value'] = getModelCount(queryset)
        else:
            filterFields = {}
            tempAnalyticHandle = tempAnalyticHandle[1:]
            for val in range(len(tempAnalyticHandle)-1):
                filterFields[tempAnalyticHandle[val]] = tempAnalyticHandle[val + 1]
            tempQuery = queryFilters.dynamicQuerysetFilter(queryset, filterFields)
            output['data'] =  getModelCountHistory(tempQuery)
            output['labels'] = getHistoryLabels(tempQuery)
            output['value'] = getModelCount(tempQuery)
    else:
        # TODO special analytics cases
        tempOutput = ANALYTICS_DICT.get(analyticsHandle, None)
        tempOutput = tempOutput(date_from, date_to)
        if tempOutput:
            output = tempOutput
    return output


class AnalyticsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None, *args, **kwrags):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        analyticsHandle = self.kwargs.get('analytics_handle', None)
        if not analyticsHandle:
            return HttpResponseNotFound('missing parameter: "analytics_handle"')
        dateFrom = None
        dateTo = None
        for param, value in request.GET.items():
            if param == 'date_from':
                dateFrom = datetime.strptime(value, '%d-%m-%Y')
            elif param == 'date_to':
                dateTo = datetime.strptime(value, '%d-%m-%Y')
        output = handleAnalytic(analyticsHandle, dateFrom, dateTo)
        if output == None:
            return HttpResponseNotFound('analytic not found for {0}'.format(analyticsHandle))
        return JsonResponse(output, content_type="application/json")