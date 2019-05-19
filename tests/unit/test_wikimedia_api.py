""" Module that defines the TestWikimediaApi class """

from app.main.classes.Wikimedia_api import Wikimedia_api

class TestWikimediaApi:
    """
    GIVEN a coordinates and a route
    WHEN the Wikimedia_api Class is instanciated
    THEN check if the method get_about return expected value
    """
    coord = {'lat': 48.8747265, 'lng': 2.3505517}
    route = 'Cité Paradis'
    about = WikimediaApi(coord, route)

    def test_wikimedia_api(self):
        assert self.about.get_about() == {
            "about_text": "La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43, rue de Paradis, la deuxième au 57, rue d'Hauteville et la troisième en impasse.",
            'about_url': "https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis"}