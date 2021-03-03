"""
Custom analytics
"""

# Django
from django.db.models import Count

# Models
from ..models import *

# Helpers
from ..helpers import queryFilters, helperDictionaries

# Datetime
import datetime
from datetime import datetime as datetimemodule
from datetime import timedelta

ALL_MONTHS_ESP = {
    'enero':  1,
    'febrero': 2,
    'marzo': 3,
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto': 8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12,
}


def getModelCount(queryset):
    return queryset.count()


# Returns the cound of a field given a year
def getModelCountHistory(queryset, year=None): # TODO: get current year
    if (year == None):
        year = datetimemodule.now().year
    outputList = []
    for key, value in ALL_MONTHS_ESP.items():
        # American format
        dateFrom = datetimemodule.strptime('{0}-1-{1}'.format(value, year), '%m-%d-%Y').date()
        nextMonth = dateFrom.replace(day=28) + timedelta(days=4)
        dateTo =  nextMonth - timedelta(days=nextMonth.day)
        temp_query = queryFilters.dynamicQuerysetFilter(queryset, None, dateFrom, dateTo, None)
        outputList.append(getModelCount(temp_query))
    return outputList


def getHistoryLabels(queryset):
    return [*ALL_MONTHS_ESP.keys()]


# custom functions start

def entrepreneursAges(dateFrom=None, dateTo=None):
    """
    Returns all entrepreneurs ages count between a set of ranges
    """
    age_ranges = [18, 40, 60, 80]
    queryset = Entrepreneur.objects
    output = {
        'data': [],
        'labels': [],
        'value': None,
    }

    for r in range(len(age_ranges)-1):
        pastDateRange = datetimemodule.now() - timedelta(days=age_ranges[r]*365) # Same day as today but X years before
        pastDateNextRange = datetimemodule.now() - timedelta(days=age_ranges[r+1]*365)
        if (dateFrom):
            queryset = queryset.filter(created_at__gte=dateFrom)
        if (dateTo):
            queryset = queryset.filter(created_at__lte=dateTo)
        output['data'].append(queryset.filter(date_of_birth__lte=pastDateRange, date_of_birth__gt=pastDateNextRange).count())
        output['labels'].append('{0}-{1}'.format(age_ranges[r], age_ranges[r+1]-1))

    return output


def projectsIncubated(dateFrom=None, dateTo=None):
    """
    Returns all projects incubated between a set of ranges (if given)
    """
    queryset = Project.objects
    output = {
        'data': [],
        'labels': [],
        'value': None,
    }
    if (dateFrom):
        queryset = queryset.filter(created_at__gte=dateFrom)
    if (dateTo):
        queryset = queryset.filter(created_at__lte=dateTo)
    stages = Stage.objects.filter(stage_type="IN")
    queryset = queryset.filter(id__in=stages.values('project_id'))
    output['data'] =  getModelCountHistory(queryset)
    output['labels'] = getHistoryLabels(queryset)
    output['value'] = getModelCount(queryset)
    return output


def projectsPreincubated(dateFrom=None, dateTo=None):
    """
    Returns all projects incubated between a set of ranges (if given)
    """
    queryset = Project.objects
    output = {
        'data': [],
        'labels': [],
        'value': None,
    }
    if (dateFrom):
        queryset = queryset.filter(created_at__gte=dateFrom)
    if (dateTo):
        queryset = queryset.filter(created_at__lte=dateTo)
    stages = Stage.objects.filter(stage_type="PI")
    queryset = queryset.filter(id__in=stages.values('project_id'))
    output['data'] =  getModelCountHistory(queryset)
    output['labels'] = getHistoryLabels(queryset)
    output['value'] = getModelCount(queryset)
    return output


def entrepreneursIncubated(dateFrom=None, dateTo=None):
    """
    Returns all entrepreneurs ages count between a set of ranges
    """
    queryset = Stage.objects
    output = {
        'data': [],
        'labels': [],
        'value': 0,
    }
    if (dateFrom):
        queryset = queryset.filter(created_at__gte=dateFrom)
    if (dateTo):
        queryset = queryset.filter(created_at__lte=dateTo)
    queryset = queryset.filter(stage_type="IN").order_by('created_at')
    projects = Project.objects.filter(id__in=queryset.values('project_id'))
    entrepreneurs = Entrepreneur.objects.filter(id__in=projects.values('entrepreneurs'))
    output['data'] = getModelCountHistory(queryset)
    output['value'] = entrepreneurs.count()
    output['labels'] = getHistoryLabels(queryset)
    return output


def entrepreneursSex(dateFrom=None, dateTo=None):
    """
    Returns all entrepreneurs sex count between a set of sex
    """
    sex_ranges = Entrepreneur.SEX_CHOICES
    queryset = Entrepreneur.objects
    output = {
        'data': [],
        'labels': [],
        'value': None,
    }

    for r in range(len(sex_ranges)):
        if (dateFrom):
            queryset = queryset.filter(created_at__gte=dateFrom)
        if (dateTo):
            queryset = queryset.filter(created_at__lte=dateTo)
        output['data'].append(queryset.filter(sex=sex_ranges[r][0]).count())
        output['labels'].append(sex_ranges[r])
    return output

def projectsSecondSeed(dateFrom=None, dateTo=None):
    """
    Returns all projects that have a second capital seed 
    """
    queryset = Project.objects
    output = {
        'data': [],
        'labels': [],
        'value': None,
    }
    if (dateFrom):
        queryset = queryset.filter(created_at__gte=dateFrom)
    if (dateTo):
        queryset = queryset.filter(created_at__lte=dateTo)
    financings = Financing.objects.filter(code_type="A2").order_by('created_at')
    queryset = Project.objects.filter(id__in=financings.values('project_id'))
    output['data'] =  getModelCountHistory(queryset)
    output['labels'] = getHistoryLabels(queryset)
    output['value'] = getModelCount(queryset)
    return output

def inscriptionsSex(dateFrom=None, dateTo=None):
    """
    Returns all inscriptiosn sex count between a set of sex
    """
    sex_ranges = Entrepreneur.SEX_CHOICES
    queryset = Inscription.objects
    output = {
        'data': [],
        'labels': [],
        'value': None,
    }

    for r in range(len(sex_ranges)):
        if (dateFrom):
            queryset = queryset.filter(created_at__gte=dateFrom)
        if (dateTo):
            queryset = queryset.filter(created_at__lte=dateTo)
        output['data'].append(queryset.filter(sex=sex_ranges[r][0]).count())
        output['labels'].append(sex_ranges[r])
    return output

def inscriptionsProvinces(dateFrom=None, dateTo=None):
    """
    Returns all inscriptions provinces history
    """
    province_ranges = Province.objects.all()
    queryset = Inscription.objects
    output = {
        'data': [],
        'labels': [],
        'value': None,
    }

    for r in range(len(province_ranges)):
        if (dateFrom):
            queryset = queryset.filter(created_at__gte=dateFrom)
        if (dateTo):
            queryset = queryset.filter(created_at__lte=dateTo)
        output['data'].append(queryset.filter(province=province_ranges[r]).count())
        output['labels'].append(province_ranges[r].name)
    return output


ANALYTICS_DICT = {
    'entrepreneurs_ages': entrepreneursAges,
    'entrepreneurs_incubated': entrepreneursIncubated,
    'entrepreneurs_sex': entrepreneursSex,
    'projects_incubated': projectsIncubated,
    'projects_preincubated': projectsPreincubated,
    'projects_second_seed': projectsSecondSeed,
    'inscriptions_sex': inscriptionsSex,
    'inscriptions_provinces': inscriptionsProvinces,
}