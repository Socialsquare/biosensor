"""
biobricks urlconf

biobricks:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d{1,2}[a-z])$', views.show, name='show'),
    url(r'^biosensorer/(\d+)$', views.show_biosensor, name='show_biosensor'),
    url(r'^biosensorer/ny$', views.new_biosensor, name='new_biosensor'),
    url(r'^biosensorer/slet/(\d+)$', views.delete_biosensor, name='delete_biosensor'),
    url(r'^biosensorer/rediger/(\d+)$', views.edit_biosensor, name='edit_biosensor'),
    url(r'^rapporter/(\d+)$', views.show_report, name='show_report'),
]
