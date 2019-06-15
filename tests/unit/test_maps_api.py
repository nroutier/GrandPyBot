""" Module that defines the unit tests for tha MapsApi class """

from app.main.classes.Maps_api import MapsApi
import os
import requests
import pytest


class MockMapsSuccessResponse:
    """ Class defining a Mock for a success request to Maps Geocode Api"""
    def __init__(self):
        self.status_code = 200

    def json(self):
        return {
            "results": [
                {
                    "formatted_address": '7 Cité Paradis, 75010 Paris, France',
                    "address_components": [
                        {
                            "long_name": "7",
                            "short_name": "7",
                            "types": [
                                "street_number"
                            ]
                        },
                        {
                            "long_name": "Cité Paradis",
                            "short_name": "Cité Paradis",
                            "types": [
                                "route"
                            ]
                        }],
                    "geometry": {
                        "location": {
                            "lat": 48.8747265,
                            "lng": 2.3505517
                        }
                    }
                }
            ]
        }


@pytest.fixture
def mock_maps_success_response(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockMapsSuccessResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    monkeypatch.delattr("requests.sessions.Session.request")


def test_req_success_status(mock_maps_success_response):
    place = MapsApi("openclassrooms")
    assert place.status == 200


def test_success_get_address(mock_maps_success_response):
    place = MapsApi("openclassrooms")
    assert place.get_address() == '7 Cité Paradis, 75010 Paris, France'


def test_success_get_route(mock_maps_success_response):
    place = MapsApi("openclassrooms")
    assert place.get_route() == 'Cité Paradis'


def test_success_get_coord(mock_maps_success_response):
    place = MapsApi("openclassrooms")
    assert place.get_coord() == {'lat': 48.8747265, 'lng': 2.3505517}


class MockMapsFailedResponse:
    def __init__(self):
        self.status_code = 404


@pytest.fixture
def mock_maps_failed_response(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockMapsFailedResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    monkeypatch.delattr("requests.sessions.Session.request")


def test_req_failed_status(mock_maps_failed_response):
    place = MapsApi("openclassrooms")
    assert place.status == 404


def test_failed_get_address(mock_maps_failed_response):
    place = MapsApi("openclassrooms")
    assert place.get_address() == ""


def test_failed_get_route(mock_maps_failed_response):
    place = MapsApi("openclassrooms")
    assert place.get_route() == ""


def test_failed_get_coord(mock_maps_failed_response):
    place = MapsApi("openclassrooms")
    assert place.get_coord() == ""
