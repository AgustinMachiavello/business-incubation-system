
# Django
from django.urls import include, path

# Views
from .views.reportgenerator import (
    ReportGeneratorView,
)
from .views.analytics import AnalyticsView
from .views.status import StatusReport

# /<page>
urlpatterns = [
    path('export/<str:file_format>/<str:analytics_handle>/', ReportGeneratorView.as_view(), name='exportreport'),
    #path('export/xls/<str:analytics_handle>/', ReportGeneratorView.as_view(), name='exportxls'),
    path('analytics/<str:analytics_handle>/', AnalyticsView.as_view(), name='analytics'),
    #path('status/<str:addresse>/', StatusReport.as_view(), name='statusreport'),
    path('status/', StatusReport.as_view(), name='statusreport'),
]
