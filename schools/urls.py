"""
schools urlconf

schools:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^teachers/signup$', views.signup_teacher, name='signup_teacher'),
]
