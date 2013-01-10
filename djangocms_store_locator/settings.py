from django.conf import settings
from django.utils.translation import ugettext_lazy as _

DJANGOCMS_STORE_LOCATOR_USE_IMPERIAL = getattr(settings, 'DJANGOCMS_STORE_LOCATOR_USE_IMPERIAL', False)
DISTANCE_CONSTANT = 3956 if DJANGOCMS_STORE_LOCATOR_USE_IMPERIAL else 6371

DISTANCE_CHOICES = getattr(settings, 'DJANGOCMS_STORE_LOCATOR_DISTANCE_CHOICES', False)
if not DISTANCE_CHOICES:
    if DJANGOCMS_STORE_LOCATOR_USE_IMPERIAL:
        DISTANCE_CHOICES = (
            ('5', _('5 miles')),
            ('10', _('10 miles')),
            ('20', _('20 miles')),
            ('50', _('50 miles')),
            ('100', _('100 miles')),
            ('200', _('200 miles')),
            ('500', _('500 miles')),
        )
    else:
        DISTANCE_CHOICES = (
            ('5', _('5 km')),
            ('10', _('10 km')),
            ('20', _('20 km')),
            ('50', _('50 km')),
            ('100', _('100 km')),
            ('200', _('200 km')),
            ('500', _('500 km')),
        )