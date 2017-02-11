from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tilmeld/$', views.new_student, name='signup'),
]
