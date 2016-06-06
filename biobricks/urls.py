"""
biobricks urlconf

biobricks:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)$', views.show, name='show'),
    url(r'^biosensor/(\d+)$', views.show_biosensor, name='show_biosensor')
]
