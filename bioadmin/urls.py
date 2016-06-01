from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^schools/$', views.schools, name='schools'),
    url(r'^schools/new$', views.new_school, name='new_school'),
    url(r'^biobricks/$', views.biobricks, name='biobricks'),
    url(r'^biobricks/$', views.biobricks, name='biobricks'),
    url(r'^biobricks/(detector)/new$', views.new_biobrick, name='new_biobrick'),
    url(r'^biobricks/(responder)/new$', views.new_biobrick, name='new_biobrick'),
    url(r'^biobricks/delete/(\d+)$', views.delete_biobrick, name='delete_biobrick'),
    url(r'^biobricks/edit/(\d+)$', views.edit_biobrick, name='edit_biobrick'),
    url(r'^biobricks/categories/new$', views.new_category, name='new_category'),
    url(r'^biobricks/categories/delete/(\d+)$', views.delete_category, name='delete_category'),
    url(r'^biobricks/categories/edit/(\d+)$', views.edit_category, name='edit_category'),
]
