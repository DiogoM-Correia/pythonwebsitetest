from django.db import models

# Create your models here.
class User(models.Model):
    gender              = models.CharField(max_length=1)
    title               = models.CharField(max_length=2)
    first               = models.TextField()
    last                = models.TextField()
    street              = models.TextField()
    city                = models.TextField()
    state               = models.TextField()
    postcode            = models.IntegerField()
    latitude            = models.TextField()
    longitude           = models.TextField()
    offset              = models.TextField()
    description         = models.TextField()
    email               = models.EmailField()
    dob_date            = models.TextField()
    dob_age             = models.TextField()
    registered_date     = models.TextField()
    registered_age      = models.TextField()
    phone               = models.TextField()
    cell                = models.TextField()
    picture_large       = models.TextField()
    picture_medium      = models.TextField()
    picture_thumbnail   = models.TextField()
