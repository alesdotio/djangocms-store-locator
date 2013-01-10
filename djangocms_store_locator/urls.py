from django.conf.urls.defaults import *
from djangocms_store_locator import views

urlpatterns = patterns('',
    url(r'^get_lat_long/$', views.get_lat_long, name='get_lat_long_url'),
    url(r'^get_locations/$', views.get_locations, name='get_locations_url'),
)
