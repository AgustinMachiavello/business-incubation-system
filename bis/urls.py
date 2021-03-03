"""bis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from ajax_select import urls as ajax_select_urls

from .apps.accounts.urls import UserLogin

urlpatterns = [
    path('', UserLogin.as_view(), name='root'),
    # Start Custom Apps
    # Accounts app
    path('', include(('bis.apps.accounts.urls', 'users'), namespace='users')),
    # Gepian Dashboard app
    path('', include(('bis.apps.gepiandashboard.urls', 'gepian'), namespace='gepian')),
    # Incubator app
    path('', include(('bis.apps.incubator.urls', 'incubator'), namespace='incubator')),
    # End Custom Apps
    # Admin panel
    path('admin/', admin.site.urls),

    # Password recovery
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Ajax Select
    path('ajax_select/', include(ajax_select_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
