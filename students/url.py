from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^elev/tilmeld$', views.new_student, name='new_student'),
]
