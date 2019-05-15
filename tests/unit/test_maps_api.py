import pytest
from app.main.classes.Maps_api import Maps_api

def test_maps_api():
    """
    GIVEN a query
    WHEN the Maps_api Class is instanciated
    THEN check if the methods get_address, get_route and get_coord return expected values
    """
    query = "openclassrooms"
    place = Maps_api(query)
    assert place.get_address() == '7 Cité Paradis, 75010 Paris, France'
    assert place.get_route() == 'Cité Paradis'
    assert place.get_coord() == {'lat': 48.8747265, 'lng': 2.3505517}