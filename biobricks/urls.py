"""
biobricks urlconf

biobricks:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d[a-z])$', views.show, name='show'),
    url(r'^catalog/biosensors/(\d+)$', views.show_biosensor, name='show_biosensor'),
    url(r'^catalog/biosensors/new$', views.new_biosensor, name='new_biosensor'),
    url(r'^catalog/biosensors/delete/(\d+)$', views.delete_biosensor, name='delete_biosensor'),
    url(r'^catalog/biosensors/edit/(\d+)$', views.edit_biosensor, name='edit_biosensor'),
]
