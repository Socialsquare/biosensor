"""
studentgroups urlconf

studentgroups:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^biosensors/(\d+)/reports/new$', views.new_report, name='new_report')
]
