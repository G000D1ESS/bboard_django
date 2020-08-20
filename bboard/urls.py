from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, PasswordResetDoneView

from .views import *

app_name = 'bboard'

urlpatterns = [

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
    path('accounts/reset_password/done',
        PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/', BbRedirectView.as_view(), name='old_detail')
]