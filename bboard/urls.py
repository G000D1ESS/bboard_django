from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

app_name = 'bboard'

urlpatterns = [
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('account/login', LoginView.as_view(), name='login'),
    path('account/logout', LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('edit/<int:pk>', BbEditView.as_view(), name='edit'),
    path('delete/<int:pk>', BbDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', BbDetailView.as_view(), name='detail'),
    path('detail/<int:year>/<int:month>/<int:day>/<int:pk>', BbRedirectView.as_view(), name='old_detail')
]