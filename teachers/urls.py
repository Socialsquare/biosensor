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
    url(r'^klasse/ny/$', views.new_school_class, name='new_school_class'),
    url(r'^klasse/(\d+)$', views.show_school_class, name='show_school_class'),
    url(r'^klasse/(\d+)/code$', views.new_school_class_code, name='new_school_class_code'),
    url(r'^$', views.dashboard, name='dashboard'),
]
