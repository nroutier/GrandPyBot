""" Module that defines the TestMapsApi class """

from app.main.classes.Maps_api import MapsApi
import os


class TestMapsApi:
    """
    GIVEN a query
    WHEN the Maps_api Class is instanciated
    THEN check if the methods get_address, get_route and get_coord return expected values
    """
    query = "openclassrooms"
    place = MapsApi(query)

    def test_get_address(self):
        assert self.place.get_address() == '7 Cité Paradis, 75010 Paris, France'

    def test_get_route(self):
        assert self.place.get_route() == 'Cité Paradis'

    def test_get_coord(self):
        # assert self.place.get_coord() == {'lat': 48.8747265, 'lng': 2.3505517}
        assert self.place.get_coord() == {'lat': 48.8748465, 'lng': 2.3504873}
