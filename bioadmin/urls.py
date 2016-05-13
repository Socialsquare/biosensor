from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schools/$', views.schools, name='schools'),
    url(r'^schools/new$', views.new_school, name='new_school'),
]
