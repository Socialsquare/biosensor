"""
studentgroups urlconf

studentgroups:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^biosensorer/(\d+)/rapporter/ny$', views.new_report, name='new_report'),
    url(r'^biosensorer/(\d+)/rapporter/rediger/(\d+)$', views.edit_report, name='edit_report')
]
