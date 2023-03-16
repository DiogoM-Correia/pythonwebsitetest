import json
from django.core import serializers
from users.models import User

persons = User.objects.all()
data = serializers.serialize('json', persons)
data = json.loads(data)

for item in data:
    fields = item['fields']
    fields['name'] = {
        'title': fields.pop('name_title'),
        'first': fields.pop('name_first'),
        'last': fields.pop('name_last')
    }
    fields['location'] = {
        'region': fields.pop('location_region'),
        'street': fields.pop('location_street'),
        'city': fields.pop('location_city'),
        'state': fields.pop('location_state'),
        'postcode': fields.pop('location_postcode'),
        'coordinates': {
            'latitude': fields.pop('location_latitude'),
            'longitude': fields.pop('location_longitude')
        },
        'timezone': {
            'offset': fields.pop('location_timezone_offset'),
            'description': fields.pop('location_timezone_description')
        }
    }
    fields['telephoneNumbers'] = fields.pop('telephone_numbers')
    fields['mobileNumbers'] = fields.pop('mobile_numbers')
    fields['picture'] = {
        'large': fields.pop('picture_large'),
        'medium': fields.pop('picture_medium'),
        'thumbnail': fields.pop('picture_thumbnail')
    }

    # Remove the model and pk fields
    item.pop('model')
    item.pop('pk')

print(json.dumps(data, indent=2))
