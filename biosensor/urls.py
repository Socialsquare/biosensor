from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^teachers/', include('teachers.urls', namespace='teachers')),
    url(r'^students/', include('studentgroups.urls', namespace='studentgroups')),
    url(r'^biobrick/', include('biobricks.urls', namespace='biobricks')),
    url(r'^bio-admin/', include('bioadmin.urls', namespace='bioadmin')),
    url(r'^$', views.homepage, name='homepage'),
]
