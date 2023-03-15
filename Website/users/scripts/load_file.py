import csv
import os
from django.conf import settings
from users.models import User
import users.scripts.params as p
import phonenumbers as pn
from django.http import JsonResponse
from users.resources import UserResource

def import_csv (filename):
    # file = open()
    
    with open(os.path.join(settings.MEDIA_ROOT, filename), 'r', encoding='utf-8') as file:
        
        reader = csv.reader(file)
        next(reader)
        i = 1

        for row in reader:
            print(i)
            i+=1

            user = User(
                type                = bounding_box_definition(float(row[8]), float(row[9])),
                gender              = gender_simply(row[0]),
                street              = row[4],  
                city                = row[5],
                state               = row[6],
                postcode            = row[7],
                latitude            = row[8],
                longitude           = row[9],
                offset              = row[10],
                description         = row[11],
                email               = row[12],
                birthday            = row[13],
                registered          = row[15],
                large               = row[19],
                medium              = row[20],
                thumbnail           = row[21]
                )
            
            # Name Class
            user.name.title = row[1]
            user.name.first = row[2]
            user.name.last  = row[3]

            print(user.name.title)
            
            # Convert phones numbers
            user.telephoneNumbers = replace_number_format(row[17], user.nacionality)
            user.mobileNumbers  = replace_number_format(row[18], user.nacionality)

            # Save new user
            user.save()

            person_resource = UserResource()
            dataset = person_resource.export()
            print(dataset.json)

def bounding_box_definition (lat, lon):

    if ((p.min_lat_special_1 <= lat <= p.max_lat_special_1 and p.min_lon_special_1 <= lon <= p.max_lon_special_1)
        or (p.min_lat_special_2 <= lat <= p.max_lat_special_2 and p.min_lon_special_2 <= lon <= p.max_lon_special_2)):

        return "ESPECIAL"
    
    elif (p.min_lat_normal <= lat <= p.max_lat_normal and p.min_lon_normal <= lon <= p.max_lon_normal):

        return "NORMAL"
    
    return "TRABALHOSO"

def replace_number_format(number, country):

    characters_to_remove = [' ', '(', ')', '-']

    for item in characters_to_remove:
        number = number.replace(item, '')

    return '+' + str(pn.country_code_for_region (country)) + number

def gender_simply (gender):

    if (gender == 'male'):
        return 'M'
    elif (gender == 'female'):
        return 'F'
    else:
        return 'ERROR'