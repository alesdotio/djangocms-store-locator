from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from djangocms_store_locator.models import StoreLocator, LocationType
from djangocms_store_locator.settings import DISTANCE_CHOICES


class StoreLocatorPlugin(CMSPluginBase):
    model = StoreLocator
    name = _('Store Locator Plugin')
    render_template = 'djangocms_store_locator/store_locator_map.html'
    admin_preview = False

    def render(self, context, instance, placeholder):
        get_lat_long_url = reverse('get_lat_long_url')
        get_locations_url = reverse('get_locations_url')
        location_types = instance.show_location_types.all() or LocationType.objects.all()
        location_types_selected = instance.show_location_types.all().exists()
        context.update({
            'get_lat_long_url': get_lat_long_url,
            'get_locations_url': get_locations_url,
            'instance': instance,
            'distance_choices': DISTANCE_CHOICES,
            'location_types': location_types,
            'location_types_selected': location_types_selected,
        })
        return context

plugin_pool.register_plugin(StoreLocatorPlugin)
