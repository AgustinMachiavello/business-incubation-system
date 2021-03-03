"""Dashboard app urls.py"""

# Django
from django.urls import include, path

# Django REST Framework
# from rest_framework.routers import DefaultRouter

# Views
from .views.dashboard import DashboardIndex
from .views.reports import ReportsIndex
from .views.administration import AdministrationIndex
from .views.postulation import PostulationPage


from .views.genericActions import (
    GenericAddModel,
    GenericListModel,
    GenericEditModel,
    GenericModelReportPage,
    GenericDeleteModel,
    GenericActivityInscription,
    GenericQuickViewModel,
)

# /<page>
urlpatterns = [
    path('dashboard/', DashboardIndex.as_view(), name='dashboardindex'),
    path('actions/add/<str:model>/', GenericAddModel.as_view(), name='genericaddmodel'),
    path('actions/list/<str:model>/', GenericListModel.as_view(), name='genericlistmodel'),
    path('actions/edit/<str:model>/<int:id>/', GenericEditModel.as_view(), name='genericeditmodel'),
    path('actions/delete/<str:model>/<int:id>/', GenericDeleteModel.as_view(), name='genericdeletemodel'),
    path('actions/view/<str:model>/<int:id>/', GenericQuickViewModel.as_view(), name='genericviewmodel'),
    path('reports/', ReportsIndex.as_view(), name='reportsindex'),
    path('reports/<str:model>/', GenericModelReportPage.as_view(), name='genericmodelreport'),
    path('administration/', AdministrationIndex.as_view(), name='administrationindex'),
    path('postulate/', PostulationPage.as_view(), name='postulate'),
    path('inscription/<str:inscription_code>/'.format(), GenericActivityInscription.as_view(), name='inscription'),
]
