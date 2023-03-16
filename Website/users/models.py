from django.db import models

# Create your models here

class User(models.Model):
    
    type                = models.CharField(max_length=20)
    gender              = models.CharField(max_length=1)
    title               = models.CharField(max_length=2)
    first               = models.CharField(max_length=50)
    last                = models.CharField(max_length=50)
    region              = models.CharField(max_length=15, null = True, default= 'Sul')
    street              = models.CharField(max_length=100)
    city                = models.CharField(max_length=50)
    state               = models.CharField(max_length=50)
    postcode            = models.IntegerField()
    latitude            = models.CharField(max_length=15)
    longitude           = models.CharField(max_length=15)
    offset              = models.CharField(max_length=10)
    description         = models.CharField(max_length=200)
    email               = models.EmailField()
    birthday            = models.DateTimeField()
    registered          = models.DateTimeField()
    telephoneNumbers    = models.CharField(max_length=20)
    mobileNumbers       = models.CharField(max_length=20)
    large               = models.URLField()
    medium              = models.URLField()
    thumbnail           = models.URLField()
    nacionality         = models.CharField(max_length=2, default='BR')

    # def __str__(self):
    #     return f"{self.title} {self.first} {self.last}"

    def to_dict(self):
        return {
            "type": self.type,
            "gender": self.gender,
            "name": {
                "title": self.title,
                "first": self.t,
                "last": self.last
            },
            "location": {
                "region": self.region,
                "street": self.street,
                "city": self.city,
                "state": self.state,
                "postcode": self.postcode,
                "coordinates": {
                    "latitude": self.latitude,
                    "longitude": self.longitude
                },
                "timezone": {
                    "offset": self.timezone_offset,
                    "description": self.timezone_description
                }
            },
            "email": self.email,
            "birthday": self.birthday.isoformat() + 'Z',
            "registered": self.registered.isoformat() + 'Z',
            "telephoneNumbers": self.telephoneNumbers,
            "mobileNumbers": self.mobileNumbers,
            "picture": {
                "large": self.large,
                "medium": self.medium,
                "thumbnail": self.thumbnail
            },
            "nationality": self.nationality
        }
    