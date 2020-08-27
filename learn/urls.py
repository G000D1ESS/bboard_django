
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', include('bboard.urls'), name=''),
    path('admin/', admin.site.urls),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/change_password/',
         PasswordChangeView.as_view(
             template_name='registration/change_password.html'),
         name='password_change'),
    path('accounts/reset_password/',
         PasswordResetView.as_view(
             template_name='registration/reset_password.html',
             subject_template_name='registration/mail/reset_subject.txt',
             email_template_name='registration/mail/reset_email.txt'),
         name='reset_password'),
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='registration/confirm_password.html'),
         name='password_reset_confirm'),
    path('accounts/reset_password/done',
         PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/done',
         PasswordResetCompleteView.as_view(
             template_name='registration/password_confirmed.html'
         ),
         name='password_reset_complete'),
]
