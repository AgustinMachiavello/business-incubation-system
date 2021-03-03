from django import template
from django.urls import reverse
from ...incubator.helpers.helperDictionaries import getDisplayName, getObject, getModelQuickViewSerializerLabel
from django.db.models.query import QuerySet

register = template.Library()

@register.filter
def get_item(dictionary, key, pk=None):
    return dictionary.get(key, None)

@register.filter
def get_foreign_key_item(dictionary, key):
    pk = dictionary.get(key, None)
    instance = getObject(key[:-3]+'s', pk) #TODO what if a model handle does not end with an S
    if not instance:
        return key
    else:
        return instance

@register.filter
def get_listing_url(argument):
    return reverse("gepian:genericlistmodel", kwargs={'model': argument})

@register.filter
def get_report_export_url(argument, fileFormat):
    if not argument:
        return None
    return reverse("incubator:exportreport", kwargs={'analytics_handle': argument, 'file_format': fileFormat})

@register.filter
def get_filter_label(argument):
    return argument.split("|")[1]

@register.filter
def get_filter_param(argument):
    return argument.split("|")[0]

@register.filter
def get_display_name(field_name, model_handle):
    return getDisplayName(field_name, model_handle) or ''

@register.filter
def get_field_display_label(field_name, model_handle):
    return getModelQuickViewSerializerLabel(field_name, model_handle)

@register.filter
def substract(a, b):
    if type(a) == QuerySet:
        a = a.count()
    if type(b) == QuerySet:
        b = b.count()
    return a - b

@register.filter
def filter_query(query, field_name_and_value):
    field_name = field_name_and_value.split(',')[0]
    field_value = field_name_and_value.split(',')[1]
    return query.filter(**{field_name: field_value}).count()

@register.filter
def addstr(a, b):
    return str(a) + str(b)
