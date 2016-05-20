from django.conf.urls import include, url
from django.contrib import admin
import bioadmin
from . import views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^schools/', include('schools.urls', namespace='schools')),
    url(r'^admin/', admin.site.urls),
    url(r'^bio-admin/', include('bioadmin.urls', namespace='bioadmin')),
    url(r'^$', views.homepage, name='homepage'),
]
