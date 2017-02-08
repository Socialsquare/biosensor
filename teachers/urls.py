"""
teachers urlconf

teachers :url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tilmeld$', views.signup, name='signup'),
    url(r'^elevgruppe/ny$', views.new_student_group, name='new_student_group'),
    url(r'^elevgruppe/slet/(?P<student_group_id>\d+)$', views.delete_student_group, name='delete_student_group'),
    url(r'^elevgruppe/rediger/(?P<student_group_id>\d+)$', views.edit_student_group, name='edit_student_group'),
    url(r'^elevgruppe/rapporter/(\d+)$', views.show_student_report, name='show_student_report'),
    url(r'^invitation/ny$', views.new_invitation, name='new_invitation'),
    url(r'^$', views.dashboard, name='dashboard'),
]
