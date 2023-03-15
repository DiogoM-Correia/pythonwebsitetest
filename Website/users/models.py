from django.db import models

# Create your models here
class Name(models.Model):

    title               = models.CharField(max_length=2)
    first               = models.TextField()
    last                = models.TextField()

class User(models.Model):
    
    type                = models.TextField()
    gender              = models.CharField(max_length=1)
    name = models.OneToOneField(
        Name,
        on_delete=models.CASCADE,
    )
    region              = models.TextField(null = True)
    street              = models.TextField()
    city                = models.TextField()
    state               = models.TextField()
    postcode            = models.IntegerField()
    latitude            = models.TextField()
    longitude           = models.TextField()
    offset              = models.TextField()
    description         = models.TextField()
    email               = models.EmailField()
    birthday            = models.TextField()
    registered          = models.TextField()
    telephoneNumbers    = models.TextField()
    mobileNumbers       = models.TextField()
    large               = models.TextField()
    medium              = models.TextField()
    thumbnail           = models.TextField()
    nacionality         = models.CharField(max_length=2, default='BR')