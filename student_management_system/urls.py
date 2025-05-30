"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from students.views import custom_login
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('accounts/', include([
        path('', RedirectView.as_view(url='login/', permanent=True)),
        path('login/', custom_login, name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
        path('password_reset/', auth_views.PasswordResetView.as_view(
            template_name='students/password_reset.html',
            email_template_name='students/password_reset_email.html',
            subject_template_name='students/password_reset_subject.txt',
            extra_context={'title': 'Reset Password'}
        ), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='students/password_reset_done.html',
            extra_context={'title': 'Password Reset Sent'}
        ), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='students/password_reset_confirm.html',
            extra_context={'title': 'Set New Password'}
        ), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
            template_name='students/password_reset_complete.html',
            extra_context={'title': 'Password Reset Complete'}
        ), name='password_reset_complete'),
    ])),
]
