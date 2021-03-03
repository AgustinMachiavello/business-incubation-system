"""Accounts app urls.py"""

# Django
from django.urls import include, path
from django.contrib.auth import views as auth_views

# Django REST Framework
# from rest_framework.routers import DefaultRouter

# Views
#from rest_auth.urls import LoginView, LogoutView
from .views.users import UserLogin, UserLogout

# <version>/users/<page>
urlpatterns = [
    path('', UserLogin.as_view(), name='base_login'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
