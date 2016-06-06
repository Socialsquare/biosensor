"""
studentgroups urlconf

studentgroups:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^/biosensor/new$', views.new_biosensor, name='new_biosensor'),
    url(r'^catalog/biosensor/delete/(\d+)$', views.delete_biosensor, name='delete_biosensor'),
    url(r'^catalog/biosensor/edit/(\d+)$', views.edit_biosensor, name='edit_biosensor'),
]
