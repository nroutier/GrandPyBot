""" Module that defines the unit tests for the WikimediaApi class """

from app.main.classes.Wikimedia_api import WikimediaApi
import pytest


geores_success_mock = [
    'Hôtel Bourrienne',
    'Cité Paradis',
    "Rue d'Hauteville",
    'Hôtel Botterel de Quintin',
    'Rue des Petites-Écu...s (Paris)'
    ]
geores_failed_mock = []


class wiki_page_success_mock:
    def __init__(self):
        self.content = "La cité Paradis est une voie publique située dans "\
            "le 10e arrondissement de Paris.\n\n\n== Situation et accès ==\n"\
            "La cité Paradis est une voie publique située dans le 10e "\
            "arrondissement de Paris. Elle est en forme de té, une branche "\
            "débouche au 43, rue de Paradis, la deuxième au 57, rue "\
            "d'Hauteville et la troisième en impasse.\n\nVues de la cité"\
            "\n\t\t\n\t\t\nCe site est desservi par les lignes \u2009\u200d"\
            "\u2009\u200d à la station de métro Bonne-Nouvelle et par la "\
            "ligne \u2009\u200d à la station Poissonnière.\n\n\n== Origine "\
            "du nom ==\nElle porte ce nom en raison de sa proximité avec la "\
            "rue éponyme.\n\n\n== Historique ==\nLa cité Paradis a été "\
            "aménagée sur les anciens jardins de l'hôtel Titon dont la façade"\
            " arrière est visible au fond de l'impasse.\nLa partie débouchant"\
            " rue de Paradis a été ouverte en 1893 et celle débouchant rue "\
            "d'Hauteville en 1906.\n\n\n== Références ==\n\n\n== Bibliographi"\
            "e ==\nJacques Hillairet, Dictionnaire historique des rues de "\
            "Paris, Paris, Les Éditions de Minuit, 1972, 1985, 1991, 1997 , "\
            "etc. (1re éd. 1960), 1 476 p., 2 vol.  [détail des éditions] "\
            "(ISBN 2-7073-1054-9, OCLC 466966117, présentation en ligne).\n\n"\
            "\n== Annexes ==\n\n\n=== Article connexe ===\nListe des voies du"\
            " 10e arrondissement de Paris\n\n\n=== Lien externe ===\nCité "\
            "Paradis (mairie de Paris) Portail de Paris   Portail de la route"
        self.url = "https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis"


class wiki_page_failed_mock:
    def __init__(self):
        self.content = ""
        self.url = ""


def test_geores_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return geores_success_mock

    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.geosearch",
        mock_get
    )

    coord = {'lat': 48.8747265, 'lng': 2.3505517}
    route = 'Cité Paradis'
    wiki_req = WikimediaApi(coord, route)

    assert wiki_req.geosearch() == [
        'Hôtel Bourrienne',
        'Cité Paradis',
        "Rue d'Hauteville",
        'Hôtel Botterel de Quintin',
        'Rue des Petites-Écu...s (Paris)'
        ]


def test_geores_failed(monkeypatch):
    def mock_get(*args, **kwargs):
        return geores_failed_mock

    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.geosearch",
        mock_get
    )

    coord = ""
    route = ""
    wiki_req = WikimediaApi(coord, route)

    assert wiki_req.geosearch() == []


def test_get_pagetitle_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return geores_success_mock

    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.geosearch",
        mock_get
    )

    coord = {'lat': 48.8747265, 'lng': 2.3505517}
    route = 'Cité Paradis'
    wiki_req = WikimediaApi(coord, route)

    assert wiki_req.get_pagetitle() == 'Cité Paradis'


def test_get_pagetitle_failed(monkeypatch):
    def mock_get(*args, **kwargs):
        return geores_failed_mock

    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.geosearch",
        mock_get
    )

    coord = ""
    route = ""
    wiki_req = WikimediaApi(coord, route)

    assert wiki_req.get_pagetitle() == ""


def test_get_about_success(monkeypatch):
    def geo_mock_get(*args, **kwargs):
        return geores_success_mock

    def page_mock_get(*args, **kwargs):
        return wiki_page_success_mock()

    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.geosearch",
        geo_mock_get
    )
    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.page",
        page_mock_get
    )

    coord = {'lat': 48.8747265, 'lng': 2.3505517}
    route = 'Cité Paradis'
    wiki_req = WikimediaApi(coord, route)

    assert wiki_req.get_about() == {
            "about_text": "La cité Paradis est une voie publique située "
            "dans le 10e arrondissement de Paris. Elle est en forme de té, "
            "une branche débouche au 43, rue de Paradis, la deuxième au 57, "
            "rue d'Hauteville et la troisième en impasse.",
            'about_url': "https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis"
            }


def test_get_about_failed(monkeypatch):
    def geo_mock_get(*args, **kwargs):
        return geores_failed_mock

    def page_mock_get(*args, **kwargs):
        return wiki_page_failed_mock()

    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.geosearch",
        geo_mock_get
    )
    monkeypatch.setattr(
        "app.main.classes.Wikimedia_api.MediaWiki.page",
        page_mock_get
    )

    coord = ""
    route = ""
    wiki_req = WikimediaApi(coord, route)

    assert wiki_req.get_about() == {
            "about_text": "",
            'about_url': ""
            }
