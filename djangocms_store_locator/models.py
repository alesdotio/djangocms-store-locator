import math

from filer.fields.image import FilerImageField
from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from djangocms_store_locator.settings import DISTANCE_CONSTANT, DISTANCE_CHOICES


class LocationManager(models.Manager):
    def __init__(self):
        super(LocationManager, self).__init__()

    def near(self, source_latitude, source_longitude, distance):
        queryset = super(LocationManager, self).get_query_set()
        rough_distance = distance / 2
        queryset = queryset.filter(
            latitude__range=(source_latitude - rough_distance, source_latitude + rough_distance),
            longitude__range=(source_longitude - rough_distance, source_longitude + rough_distance)
        )
        locations = []
        for location in queryset:
            if location.latitude and location.longitude:
                exact_distance = self.get_distance(source_latitude, source_longitude, location)
                if exact_distance <= distance:
                    setattr(location, 'distance', exact_distance)
                    locations.append(location)

        return locations

    def get_distance(self, source_latitude, source_longitude, target_location):
        lat_1 = math.radians(source_latitude)
        long_1 = math.radians(source_longitude)
        lat_2 = math.radians(target_location.latitude)
        long_2 = math.radians(target_location.longitude)
        dlong = long_2 - long_1
        dlat = lat_2 - lat_1
        a = (math.sin(dlat / 2))**2 + math.cos(lat_1) * math.cos(lat_2) * (math.sin(dlong / 2))**2
        c = 2 * math.asin(min(1, math.sqrt(a)))
        dist = DISTANCE_CONSTANT * c
        return dist


class LocationType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    location_types = models.ManyToManyField(LocationType, verbose_name=_('Location types'), blank=True, null=True)
    name = models.CharField(_('Name'), max_length=255)
    image = FilerImageField(verbose_name=_('Image'), blank=True, null=True)
    address = models.TextField(_('Address'), max_length=255, blank=False)
    latitude = models.FloatField(_('Latitude'), blank=False, null=True)
    longitude = models.FloatField(_('Longitude'), blank=False, null=True)
    description = models.TextField(_('Description'), blank=True, null=True)
    phone = models.CharField(_('Phone'), max_length=255, blank=True, null=True)
    url = models.URLField(_('URL'), max_length=255, blank=True, null=True)
    active = models.BooleanField(_('Active'), default=True, blank=True)

    objects = LocationManager()

    class Meta:
        verbose_name = _('Store Location')
        verbose_name_plural = _('Store Locations')

    def __unicode__(self):
        return self.name

    def get_single_line_address(self):
        return self.address.replace('\n', ', ')

    def get_image_url(self):
        if self.image:
            return self.image.url

    def has_image(self):
        if self.image:
            return True
        return False
    has_image.boolean = True


class StoreLocator(CMSPlugin):
    default_distance = models.CharField(max_length=50, default='10', choices=DISTANCE_CHOICES)
    starting_location = models.CharField(max_length=255, blank=True, help_text="A city or address to center the map on.")
    append_to_search = models.CharField(max_length=255, blank=True, help_text="Search term to append at the end of the query.")
    show_distance = models.BooleanField(default=True, help_text="Disabling this will render all locations on the map regardless of zoom level")
    show_location_types = models.ManyToManyField(LocationType, blank=True, null=True)

    def copy_relations(self, oldinstance):
        self.show_location_types = oldinstance.show_location_types.all()
