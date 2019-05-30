""" Module that defines the class Maps_api"""

from flask import current_app
import requests
import json
import os


class MapsApi:
    """ Class used to get address, route and coordinates from Google Geocode Api """

    def __init__(self, query):
        payload = {
            'key': os.environ.get('MAPS_KEY'),
            'address': query.replace(" ", "%"),
            'region': "fr",
            'country': "fr"
        }
        req = 'https://maps.googleapis.com/maps/api/geocode/json'
        r = requests.get(req, payload)
        self.res = r.json()

    def get_address(self):
        if self.res:
            try:
                address = self.res['results'][0]["formatted_address"]
            except:
                address = ""
            return address

    def get_route(self):
        if self.res:
            try:
                address_components = self.res['results'][0]["address_components"]
                i = 0
                for i in range(len(address_components)):
                    if address_components[i]['types'] == ['route']:
                        route = address_components[i]['short_name']
            except:
                route = ""
            return route

    def get_coord(self):
        if self.res:
            try:
                coord = self.res['results'][0]["geometry"]["location"]
            except:
                coord = ""
            return coord

    # def get_map_url(self):
    #     try:
    #         coord = self.get_coord()
    #         coord_url = f"{coord['lat']},{coord['lng']}"
    #         key_static_maps = os.environ.get('STATIC_MAPS_KEY')
    #         map_url = 'https://maps.googleapis.com/maps/api/staticmap?center=' + coord_url + '&zoom=15&size=400x400&markers=color:red%7C' + coord_url + '&key=' + key_static_maps
    #     except:
    #         map_url = ""
    #     return map_url
