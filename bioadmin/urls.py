from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/schools/new$', views.new_school, name='new_school'),
    url(r'^catalog/$', views.catalog, name='catalog'),
    url(r'^catalog/biosensors/(\d+)$', views.show_biosensor, name='show_biosensor'),
    url(r'^catalog/biosensors/new$', views.new_biosensor, name='new_biosensor'),
    url(r'^catalog/biosensors/delete/(\d+)$', views.delete_biosensor, name='delete_biosensor'),
    url(r'^catalog/biosensors/edit/(\d+)$', views.edit_biosensor, name='edit_biosensor'),
    url(r'^catalog/(detector)s/new$', views.new_biobrick, name='new_biobrick'),
    url(r'^catalog/(responder)s/new$', views.new_biobrick, name='new_biobrick'),
    url(r'^catalog/delete/(\d+)$', views.delete_biobrick, name='delete_biobrick'),
    url(r'^catalog/edit/(\d+)$', views.edit_biobrick, name='edit_biobrick'),
    url(r'^catalog/categories/new$', views.new_category, name='new_category'),
    url(r'^catalog/categories/delete/(\d+)$', views.delete_category, name='delete_category'),
    url(r'^catalog/categories/edit/(\d+)$', views.edit_category, name='edit_category'),
]
