import urllib2
import json
import logging
from django.http import HttpResponse
from django.utils.http import urlencode
from djangocms_store_locator.models import Location

logger = logging.getLogger('djangocms.storelocator')


def get_lat_long(request):
    args = urlencode({'address': request.GET.get('q', ''), 'sensor': 'false'})
    r = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?%s" % args)
    data = json.loads(r.read())
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latlong = location['lat'], location['lng']
    else:
        if data['status'] == 'OVER_QUERY_LIMIT':
            logger.error('Google Maps Geocoding over limit!')
        latlong = ('', '')
    return HttpResponse(','.join(map(str, latlong)))


def get_locations(request):
    try:
        latitude = float(request.GET.get('lat'))
        longitude = float(request.GET.get('long'))
        distance = int(request.GET.get('distance', 0))
        location_type = request.GET.get('location_type', '0')
    except:
        return HttpResponse('[]')
    
    locations = Location.objects.near(latitude, longitude, distance)
    if location_type:
        locations = [l for l in locations if location_type in [str(t[0]) for t in l.location_types.values_list('id')]]
    json_locations = []
    locations.sort(key=lambda loc: loc.distance)
    for location in locations:
        location_dict = dict()
        location_dict['id'] = location.id
        location_dict['name'] = location.name
        location_dict['address'] = location.address
        location_dict['latitude'] = location.latitude
        location_dict['longitude'] = location.longitude
        location_dict['distance'] = location.distance
        location_dict['description'] = location.description
        location_dict['url'] = location.url
        location_dict['phone'] = location.phone
        location_dict['image'] = location.get_image_url()
        json_locations.append(location_dict)
    return HttpResponse(json.dumps(json_locations), mimetype="application/json")
