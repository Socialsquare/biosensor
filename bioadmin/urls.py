from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schools/$', views.schools, name='schools'),
    url(r'^schools/new$', views.new_school, name='new_school'),
    url(r'^biobricks/$', views.biobricks, name='biobricks'),
    url(r'^biobricks/$', views.biobricks, name='biobricks'),
    url(r'^biobricks/categories/new$', views.new_category, name='new_category'),
    url(r'^biobricks/categories/delete/(\d+)$', views.delete_category, name='delete_category'),
    url(r'^biobricks/categories/edit/(\d+)$', views.edit_category, name='edit_category'),
]
