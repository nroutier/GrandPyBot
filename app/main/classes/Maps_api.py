""" Module that defines the class Maps_api"""

from flask import current_app
import requests
import json
import os


class MapsApi:
    """ Class used to get address, route and coordinates from
    Google Geocode Api """

    def __init__(self, query):
        payload = {
            'key': os.environ.get('MAPS_KEY'),
            'address': query.replace(" ", "%"),
            'region': "fr",
            'country': "fr"
        }
        req = 'https://maps.googleapis.com/maps/api/geocode/json'
        r = requests.get(req, payload)
        self.status = r.status_code
        if self.status == 200:
            self.res = r.json()

    def get_address(self):
        if self.status == 200:
            try:
                address = self.res['results'][0]["formatted_address"]
            except:
                address = ""
        else:
            address = ""
        return address

    def get_route(self):
        route = ""
        if self.status == 200:
            try:
                address_components = self.res['results'][0][
                    "address_components"]
                i = 0
                for i in range(len(address_components)):
                    if address_components[i]['types'] == ['route']:
                        route = address_components[i]['short_name']
            except:
                pass
        return route

    def get_coord(self):
        if self.status == 200:
            try:
                coord = self.res['results'][0]["geometry"]["location"]
            except:
                coord = ""
        else:
            coord = ""
        return coord
