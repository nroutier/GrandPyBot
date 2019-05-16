from app.main.classes.Maps_api import Maps_api
# from flask import current_app
import os

class TestMapsApi:
    """
    GIVEN a query
    WHEN the Maps_api Class is instanciated
    THEN check if the methods get_address, get_route and get_coord return expected values
    """
    query = "openclassrooms"
    place = Maps_api(query)
    key_static_maps = os.environ.get('STATIC_MAPS_KEY')
    # key_static_maps = current_app.config['STATIC_MAPS_KEY']

    def test_get_address(self):
        assert self.place.get_address() == '7 Cité Paradis, 75010 Paris, France'

    def test_get_route(self):
        assert self.place.get_route() == 'Cité Paradis'

    def test_get_coord(self):
        assert self.place.get_coord() == {'lat': 48.8747265, 'lng': 2.3505517}
    
    def test_get_map_url(self):
        # key_static_maps = app.config['STATIC_MAPS_KEY']
        assert self.place.get_map_url() == "https://maps.googleapis.com/maps/api/staticmap?center=48.8747265,2.3505517&zoom=15&size=400x400&markers=color:red%7C48.8747265,2.3505517&key=" + self.key_static_maps