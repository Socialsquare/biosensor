from django.conf.urls import url

from . import views

# TODO Kunne være rart at oversætte var detector og responder, hvis det er muligt?

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^skoler/$', views.schools, name='schools'),
    url(r'^skoler/ny$', views.new_school, name='new_school'),
    url(r'^laerer/$', views.teachers, name='teachers'),
    url(r'^elevgrupper/$', views.student_groups, name='student_groups'),
    url(r'^katalog/$', views.catalog, name='catalog'),
    url(r'^katalog/biosensorer/(\d+)$', views.show_biosensor, name='show_biosensor'),
    url(r'^katalog/biosensorer/ny$', views.new_biosensor, name='new_biosensor'),
    url(r'^katalog/biosensorer/slet/(\d+)$', views.delete_biosensor, name='delete_biosensor'),
    url(r'^katalog/biosensorer/rediger/(\d+)$', views.edit_biosensor, name='edit_biosensor'),
    url(r'^katalog/elevrapporter/(\d+)$', views.show_student_report, name='show_student_report'),
    url(r'^katalog/(detector)er/ny$', views.new_biobrick, name='new_biobrick'),
    url(r'^katalog/(responder)e/ny$', views.new_biobrick, name='new_biobrick'),
    url(r'^katalog/slet/(\d+)$', views.delete_biobrick, name='delete_biobrick'),
    url(r'^katalog/rediger/(\d+)$', views.edit_biobrick, name='edit_biobrick'),
    url(r'^katalog/kategorier/ny$', views.new_category, name='new_category'),
    url(r'^katalog/kategorier/slet/(\d+)$', views.delete_category, name='delete_category'),
    url(r'^katalog/kategorier/rediger/(\d+)$', views.edit_category, name='edit_category'),
]
