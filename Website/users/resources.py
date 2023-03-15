from import_export import resources
from .models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('type', 'gender', 'name', 'street', 'city', 'state', 'postcode', 'latitude', 'longitude', 'offset', 'descripti', 'email', 'birthday', 'registere', 'large', 'medium', 'thumbnail')

  