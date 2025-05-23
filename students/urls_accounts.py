from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .views import custom_login

app_name = 'accounts'

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=True)),
    path('login/', custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
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
] 