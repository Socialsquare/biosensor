"""
biobricks urlconf

biobricks:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(\d+)$', views.show, name='show')
]
