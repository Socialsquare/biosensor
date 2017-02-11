from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tilmeld/$', views.signup, name='signup'),
]

# The remaining urls in the 'elev' header dropdown
# are generated from static pages in Wagtail.
