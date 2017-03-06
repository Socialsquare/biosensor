"""
studentgroups urlconf

studentgroups:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.dashboard, name='dashboard'),
    url(r'^biosensor/(\d+)/photo$',
        views.update_photo, name='update_photo'),
    url(r'^biosensor/(\d+)/resume$',
        views.update_resume, name='update_resume'),
    url(r'^biosensor/(\d+)/report$',
        views.update_report, name='update_report'),
]
