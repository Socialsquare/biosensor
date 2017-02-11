# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from django.conf import settings

from . import views

urlpatterns = [
    url(r'^bruger/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^laerere/', include('teachers.urls', namespace='teachers')),
    url(r'^elev/', include('students.urls', namespace='students')),
    url(r'^elevgruppe/', include('studentgroups.urls', namespace='studentgroups')),
    url(r'^biobrick/', include('biobricks.urls', namespace='biobricks')),
    url(r'^bioadmin/', include('bioadmin.urls', namespace='bioadmin')),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^$', views.homepage, name='homepage'),
    url(r'', include(wagtail_urls)),
] + static(settings.STATIC_URL_PATTERN, document_root=settings.STATIC_ROOT) +\
    static(settings.MEDIA_URL_PATTERN, document_root=settings.MEDIA_ROOT)
