"""
Custom reports
"""

# Django
from django.db.models import Count

# Models
from ..models import *

# Helpers
from ..helpers import queryFilters, helperDictionaries



def entrepreneursIncubated(dateFrom=None, dateTo=None):
    """
    Returns all entrepreneurs ages count between a set of ranges
    """
    queryset = Stage.objects
    output = {
        'queryset': None,
        'fields': [],
        'values': [],
        'fieldLabels': [],
    }
    queryset = queryset.filter(stage_type="IN") # check for duplicated 
    projects = Project.objects.filter(id__in=queryset.values('project_id'))
    entrepreneurs = Entrepreneur.objects.filter(id__in=projects.values('entrepreneurs'))
    output['queryset'] = entrepreneurs
    fieldsDict = helperDictionaries.getModelReportFields('entrepreneurs')
    output['fieldDict'] = fieldsDict
    output['fields'] = [*fieldsDict.keys()]
    output['fieldLabels'] = [*fieldsDict.values()]
    return output


def entrepreneursSex(dateFrom=None, dateTo=None):
    """
    Returns all entrepreneurs sex count between a set of sex
    """
    queryset = Stage.objects
    output = {
        'queryset': None,
        'fields': [],
        'values': [],
        'fieldLabels': [],
    }
    queryset = queryset.filter(stage_type="IN") # check for duplicated 
    projects = Project.objects.filter(id__in=queryset.values('project_id'))
    entrepreneurs = Entrepreneur.objects.filter(id__in=projects.values('entrepreneurs'))
    output['queryset'] = entrepreneurs
    fieldsDict = helperDictionaries.getModelReportFields('entrepreneurs')
    output['fieldDict'] = fieldsDict
    output['fields'] = [*fieldsDict.keys()]
    output['fieldLabels'] = [*fieldsDict.values()]

    return output

def projectsIncubated(dateFrom=None, dateTo=None):
    """
    Returns all projects incubated between a set of ranges (if given)
    """
    queryset = Stage.objects
    output = {
        'queryset': None,
        'fields': [],
        'values': [],
        'fieldLabels': [],
    }
    queryset = queryset.filter(stage_type="IN") # check for duplicated 
    projects = Project.objects.filter(id__in=queryset.values('project_id'))
    output['queryset'] = projects
    fieldsDict = helperDictionaries.getModelReportFields('projects')
    output['fieldDict'] = fieldsDict
    output['fields'] = [*fieldsDict.keys()]
    output['fieldLabels'] = [*fieldsDict.values()]
    return output


def projectsPreincubated(dateFrom=None, dateTo=None):
    """
    Returns all projects incubated between a set of ranges (if given)
    """
    queryset = Stage.objects
    output = {
        'queryset': None,
        'fields': [],
        'values': [],
        'fieldLabels': [],
    }
    queryset = queryset.filter(stage_type="PI") # check for duplicated 
    projects = Project.objects.filter(id__in=queryset.values('project_id'))
    output['queryset'] = projects
    fieldsDict = helperDictionaries.getModelReportFields('projects')
    output['fieldDict'] = fieldsDict
    output['fields'] = [*fieldsDict.keys()]
    output['fieldLabels'] = [*fieldsDict.values()]
    return output

def projectsSecondSeed(dateFrom=None, dateTo=None):
    """
    Returns all projects that have a second capital seed 
    """
    queryset = Financing.objects
    output = {
        'queryset': None,
        'fields': [],
        'values': [],
        'fieldLabels': [],
    }
    queryset = queryset.filter(code_type="A2") # check for duplicated 
    projects = Project.objects.filter(id__in=queryset.values('project_id'))
    output['queryset'] = projects
    fieldsDict = helperDictionaries.getModelReportFields('projects')
    output['fieldDict'] = fieldsDict
    output['fields'] = [*fieldsDict.keys()]
    output['fieldLabels'] = [*fieldsDict.values()]
    return output

REPORTS_DICT = {
    'entrepreneurs_incubated': entrepreneursIncubated,
    'projects_incubated': projectsIncubated,
    'projects_preincubated': projectsPreincubated,
    'projects_second_seed': projectsSecondSeed,
}