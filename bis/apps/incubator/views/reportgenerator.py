"""XLS generator views"""

# Django
from django.shortcuts import render
from django.views.generic import View
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseServerError,
    HttpResponse
)

# Models
from ..models import (
    Entrepreneur
)

# CSV and XLS
import csv
import xlwt

# Analytics
from ..helpers import helperDictionaries, queryFilters

# Datetime
from datetime import datetime
from .customReports import REPORTS_DICT

def generateXLS(fileName, columns, values):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="{0}.xls"'.format(fileName)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(fileName)

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = columns

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = values
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


class ReportGeneratorView(View):

    def generateFileName(self, prefix=None):
        output = 'openseed_export_{0}'.format(datetime.now().year)
        if prefix:
            output = '{0}_openseed_export_{1}'.format(prefix, datetime.now().year)
        return output

    def generateReportFile(self, fileFormat, columns, values):
        if fileFormat == 'xls':
            return generateXLS(self.generateFileName(), columns, values) # TODO get current date + model
        elif fileFormat == 'csv':
            return None
        else:
            return None

    def generateValues(self, queryset, columns, fieldsDict=None):
        temp_query = queryset
        if fieldsDict:
            temp_query = queryFilters.dynamicQuerysetFilter(queryset, fieldsDict)
        values = temp_query.all().values_list(*columns)
        return values

    def getModelReportFields(self, modelHandle):
        fieldsDict = helperDictionaries.getModelReportFields(modelHandle)
        return [*fieldsDict.values()]

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'errors/401.html')
        analyticsHandle = self.kwargs.get('analytics_handle', None)
        fileFormat = self.kwargs.get('file_format', 'xls')
        fields = [] # fields to extract from the model
        values = [] # each row of values
        fieldLabels = [] # Field names displayed on top of the file
        if analyticsHandle:
            if ('__' in analyticsHandle):
                tempAnalyticHandle = analyticsHandle.split('__')
                modelHandle = tempAnalyticHandle[0]
                model = helperDictionaries.getModel(modelHandle)
                fieldsDict = helperDictionaries.getModelReportFields(modelHandle)
                fields = [*fieldsDict.keys()]
                fieldLabels = [*fieldsDict.values()]
                if ('__count' in analyticsHandle):
                    values = self.generateValues(model.objects, fields)
                else:
                    filterFields = {}
                    tempAnalyticHandle = tempAnalyticHandle[1:]
                    for val in range(len(tempAnalyticHandle)-1):
                        filterFields[tempAnalyticHandle[val]] = tempAnalyticHandle[val + 1]
                    values = self.generateValues(model.objects, fields, filterFields)
            else:
                # TODO dictionary of special report cases
                output = REPORTS_DICT.get(analyticsHandle, None)()
                fieldLabels = output['fieldLabels']
                values = self.generateValues(output['queryset'], output['fields'])
        response = self.generateReportFile(fileFormat, fieldLabels, values)
        return response

"""
class CSVGeneratorView(View):

    def exportEntrepreneurs(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(['Username', 'First name', 'Last name', 'Email address'])

        users = Entrepreneur.objects.all().values_list('username', 'first_name', 'last_name', 'email')
        for user in users:
            writer.writerow(user)

        return response

    def get(self, request, **kwargs):

        return self.exportEntrepreneurs()
"""
