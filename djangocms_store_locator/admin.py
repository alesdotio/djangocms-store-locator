from django.contrib import admin
from django.conf.urls.defaults import patterns, url
from models import Location, LocationType
from djangocms_store_locator.views import get_lat_long, get_locations
from django.utils.translation import ugettext_lazy as _


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'url', 'has_image', 'active')
    list_filter = ('active', 'location_types')
    search_fields = ('name', 'address', 'description')
    
    fieldsets = (
        (None, {
            'fields': (('name', 'active'),'location_types',)
        }),
        (_('Address'), {
            'fields': ('address', ('latitude', 'longitude'))
        }),
        (_('Other information'), {
            'fields': ('phone', 'url', 'description', 'image')
        }),
    )
    class Media:
        js = ("djangocms_store_locator/js/store_locator_admin.js",)

    def get_urls(self):
        old_urls = super(LocationAdmin, self).get_urls()
        new_urls = patterns('',
            url(r'^get_lat_long/$', get_lat_long, name='get_lat_long_url'),
            url(r'^get_locations/$', get_locations, name='get_locations_url'),
        )
        return new_urls + old_urls

admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType)

