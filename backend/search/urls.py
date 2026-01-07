from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]