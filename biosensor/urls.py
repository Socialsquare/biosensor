from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^bruger/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^laerer/', include('teachers.urls', namespace='teachers')),
    url(r'^elevgruppe/', include('studentgroups.urls', namespace='studentgroups')),
    url(r'^biobrick/', include('biobricks.urls', namespace='biobricks')),
    url(r'^bioadmin/', include('bioadmin.urls', namespace='bioadmin')),
    url(r'^$', views.homepage, name='homepage'),
]
