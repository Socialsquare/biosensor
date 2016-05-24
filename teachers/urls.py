"""
schools urlconf

schools:url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^student-groups/new$', views.new_student_group, name='new_student_group'),
    url(r'^$', views.show, name='show'),
]
