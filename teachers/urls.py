"""
teachers urlconf

teachers :url_name
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^signup$', views.signup, name='signup'),
    url(r'^student-groups/new$', views.new_student_group, name='new_student_group'),
    url(r'^student-groups/delete/(\d+)$', views.delete_student_group, name='delete_student_group'),
    url(r'^student-groups/edit/(\d+)$', views.edit_student_group, name='edit_student_group'),
    url(r'^$', views.dashboard, name='dashboard'),
]
