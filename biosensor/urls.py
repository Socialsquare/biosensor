from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from . import views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^teachers/', include('teachers.urls', namespace='teachers')),
    url(r'^students/', include('studentgroups.urls', namespace='studentgroups')),
    url(r'^biobrick/', include('biobricks.urls', namespace='biobricks')),
    url(r'^bioadmin/', include('bioadmin.urls', namespace='bioadmin')),
    url(r'^cms/', include(wagtailadmin_urls)),
    url(r'^$', views.homepage, name='homepage'),
    url(r'', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
