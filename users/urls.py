"""
profile urlconf

profile :url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profil$',
        views.profile,
        name='profile'),
]
