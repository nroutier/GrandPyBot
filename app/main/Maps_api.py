#coding: utf-8

""" Module that defines the class Maps_api"""

import os
import requests
import json

class Maps_api:
    """ Class used to get address, route and coordinates from Google Geocode Api """

    def __init__(self, query):
        payload = {
            'key': os.environ.get('MAPS_KEY'),
            'key_static_maps': os.environ.get('STATIC_MAPS_KEY'),
            'address': query.replace(" ", "%"),
            'region': "fr",
            'country': "fr"
        }
        req = 'https://maps.googleapis.com/maps/api/geocode/json'
        r = requests.get(req, payload)
        self.res = r.json()
       

    def get_address(self):
        if self.res:
            address = self.res['results'][0]["formatted_address"]
            return address

    def get_route(self):
        if self.res:
            address_components = self.res['results'][0]["address_components"]
            i = 0
            for i in range(len(address_components)):
                if address_components[i]['types'] == ['route']:
                    route = address_components[i]['short_name']
                    return route
    
    def get_coord(self):
        if self.res:
            coord = self.res['results'][0]["geometry"]["location"]
            return coord

    def get_map_url(self):
        coord = self.get_coord()
        coord_url = "{},{}".format(coord['lat'],coord['lng'])
        map_url = 'https://maps.googleapis.com/maps/api/staticmap?center=' + coord_url + '&zoom=15&size=400x400&markers=color:red%7C48.8747265,2.404306&key=' + key_static_maps
        return map_url
