
from django.contrib import admin
from django.urls import path, include

from bboard.views import index

urlpatterns = [
    path('', include('bboard.urls'), name=''),
    path('admin/', admin.site.urls),
]
